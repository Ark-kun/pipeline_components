/**
 * @license
 * Copyright 2022 Alexey Volkov
 * SPDX-License-Identifier: Apache-2.0
 * @author         Alexey Volkov <alexey.volkov+oss@ark-kun.com>
 * @copyright 2022 Alexey Volkov <alexey.volkov+oss@ark-kun.com>
 */

const fs = require("fs");
const readline = require("readline");
const path = require("path");

// Skip 1 argument when running the script using node --eval
// Skip 2 arguments when running from file: `node grep.js`.
const args = process.argv.slice(2);
const input_path = args[0];
const pattern = args[1];
const output_path = args[2];

fs.mkdirSync(path.dirname(output_path), { recursive: true });
const inputStream = fs.createReadStream(input_path);
const outputStream = fs.createWriteStream(output_path, { encoding: "utf8" });
var lineReader = readline.createInterface({
  input: inputStream,
  terminal: false,
});
lineReader.on("line", function (line) {
  if (line.match(pattern)) {
    outputStream.write(line + "\n");
  }
});
