import { WordTokenizer } from 'natural';
import * as stopword from 'stopword';

// diccionario de groserías
const profanities: string[] = [
  "puta", "menso", "idiota", "pendeja", "estúpida", "perra","culo","pendejos", 
  "pichula", "verga", "culón", "vagina", "tetas", "desgraciada", "desgraciado", "malcriada", "mierda", 
  "caca", "pene", "pito", "cagada","asqueroso", "defectuoso","cochino","maricón", "mamarracho",
  "chafa", "cagón", "pendejada", "nalgas", "pésimo", "porquería", "basura","puto",
  "horrible", "inservible", "deplorable", "maldito", "desastroso", "ratero", "chupapijas",
  "estúpido", "cagada", "pendejo", "gilipollas", "rancio", "cacas", "deshecho","cochambre","alv","calzon"
];

// Función para tokenizar el texto
const tokenizer = new WordTokenizer();

function tokenizeText(text: string): string[] {
  return tokenizer.tokenize(text.toLowerCase());
}

// stop words en español
function removeStopWords(tokens: string[]): string[] {
  return stopword.removeStopwords(tokens, stopword.spa);
}

// detectar groserías
function containsProfanity(tokens: string[]): boolean {
  return tokens.some(token => profanities.includes(token));
}

// clasificar el texto
export function classifyText(text: string): string {
  const tokens = tokenizeText(text);
  const filteredTokens = removeStopWords(tokens);
  const hasProfanity = containsProfanity(filteredTokens);

  return hasProfanity ? "El texto contiene lenguaje inapropiado." : "El texto es apropiado.";
}
