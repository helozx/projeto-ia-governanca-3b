import fs from "node:fs/promises";
import { Workbook } from "@oai/artifact-tool";

const outputCsv = process.argv[2];
const previewPng = process.argv[3];

if (!outputCsv || !previewPng) {
  throw new Error("Uso: create_dataset.mjs <saida.csv> <preview.png>");
}

const headers = [
  "id_solicitacao",
  "renda_mensal",
  "divida_total",
  "tempo_emprego_meses",
  "idade",
  "genero_simulado",
  "regiao_simulada",
  "acesso_digital",
  "score_credito",
  "pontuacao_modelo",
  "resultado",
  "decisao",
  "motivo_informado",
];

const rows = [];
for (let profile = 1; profile <= 24; profile += 1) {
  const renda = 1900 + ((profile * 617) % 6100);
  const divida = 700 + ((profile * 947) % 8300);
  const emprego = 6 + ((profile * 13) % 91);
  const idade = 20 + ((profile * 7) % 38);
  const score = 545 + ((profile * 29) % 205);
  const regiao = profile % 3 === 0 ? "Periferica" : "Central";
  const acesso = profile % 4 === 0 ? "Limitado" : "Completo";

  for (const genero of ["M", "F"]) {
    const qualidadeFinanceira =
      score +
      (renda / 1000) * 8 -
      (divida / Math.max(renda, 1)) * 18 +
      (emprego / 12) * 3;

    // Penalidades deliberadamente injustas para fins didaticos.
    const penalidadeGenero = genero === "F" ? 28 : 0;
    const penalidadeRegiao = regiao === "Periferica" ? 10 : 0;
    const penalidadeAcesso = acesso === "Limitado" ? 8 : 0;
    const pontuacaoModelo = Math.round(
      qualidadeFinanceira - penalidadeGenero - penalidadeRegiao - penalidadeAcesso,
    );
    const resultado = pontuacaoModelo >= 670 ? 1 : 0;

    rows.push([
      `SOL-${String(rows.length + 1).padStart(3, "0")}`,
      renda,
      divida,
      emprego,
      idade,
      genero,
      regiao,
      acesso,
      score,
      pontuacaoModelo,
      resultado,
      resultado === 1 ? "Aprovado" : "Negado",
      resultado === 1
        ? "Perfil dentro da faixa simulada"
        : "Pontuacao automatizada abaixo do limite",
    ]);
  }
}

const workbook = Workbook.create();
const sheet = workbook.worksheets.add("Dados");
sheet.showGridLines = false;
sheet.getRangeByIndexes(0, 0, 1, headers.length).values = [headers];
sheet.getRangeByIndexes(1, 0, rows.length, headers.length).values = rows;
sheet.getRangeByIndexes(0, 0, 1, headers.length).format = {
  fill: "#1F4E78",
  font: { name: "Arial", size: 10, bold: true, color: "#FFFFFF" },
  verticalAlignment: "center",
  horizontalAlignment: "center",
};
sheet.getRangeByIndexes(1, 0, rows.length, headers.length).format.font = {
  name: "Arial",
  size: 10,
};
const columnWidths = [16, 14, 13, 22, 10, 18, 18, 16, 14, 16, 10, 12, 38];
columnWidths.forEach((width, index) => {
  sheet.getRangeByIndexes(0, index, rows.length + 1, 1).format.columnWidth = width;
});
sheet.freezePanes.freezeRows(1);

workbook.recalculate();

const inspection = await workbook.inspect({
  kind: "table",
  sheetId: "Dados",
  range: "A1:M12",
  include: "values,formulas",
  tableMaxRows: 12,
  tableMaxCols: 13,
  maxChars: 5000,
});
console.log(inspection.ndjson);

const errorScan = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!",
  options: { useRegex: true, maxResults: 100 },
  summary: "final formula error scan",
});
console.log(errorScan.ndjson);

const preview = await workbook.render({
  sheetName: "Dados",
  range: "A1:M14",
  scale: 1,
  format: "png",
});
await fs.writeFile(previewPng, new Uint8Array(await preview.arrayBuffer()));

const escapeCsv = (value) => {
  const text = String(value ?? "");
  return /[",\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
};
const csv = [headers, ...rows]
  .map((row) => row.map(escapeCsv).join(","))
  .join("\n") + "\n";

await fs.mkdir(new URL(".", `file://${outputCsv}`).pathname, { recursive: true });
await fs.writeFile(outputCsv, csv, "utf8");

const female = rows.filter((row) => row[5] === "F");
const male = rows.filter((row) => row[5] === "M");
const rate = (group) => group.reduce((sum, row) => sum + row[10], 0) / group.length;
console.log(JSON.stringify({
  registros: rows.length,
  aprovacao_geral: rate(rows),
  aprovacao_feminino_simulado: rate(female),
  aprovacao_masculino_simulado: rate(male),
  diferenca_pontos_percentuais: (rate(male) - rate(female)) * 100,
}, null, 2));
