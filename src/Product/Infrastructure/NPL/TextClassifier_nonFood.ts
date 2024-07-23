import { WordTokenizer } from 'natural';


const nonFoodWords: string[] = [
  'camisa', 'pantalones', 'zapatos', 'bolso', 'anillo', 'collar', 'herramienta', 'martillo', 'destornillador', 
  'libro', 'cuaderno', 'lámpara', 'teléfono', 'computadora', 'coche', 'moto', 'bicicleta', 'juguete',
  'mueble', 'silla', 'mesa', 'sofá', 'cama', 'armario', 'espejo', 'reloj', 'gafas', 'pulsera', 'sombrero',
  'corbata', 'cinturón', 'mochila', 'cartera', 'billetera', 'pañuelo', 'bufanda', 'abrigo', 'chaqueta', 
  'traje', 'pijama', 'camiseta', 'polo', 'shorts', 'calcetines', 'medias', 'guantes', 'zapatillas', 
  'sandalias', 'botas', 'cazadora', 'impermeable', 'gorra', 'pasamontañas', 'traje de baño', 'bikini',
  'calzoncillos', 'bragas', 'sujetador', 'corpiño', 'bata', 'kimono', 'guantes de lana', 'guantes de cuero',
  'guantes de trabajo', 'casco', 'chaleco', 'chaleco reflectante', 'chaqueta de cuero', 'chaqueta vaquera',
  'parka', 'anorak', 'plumífero', 'gorro', 'boina', 'bufanda de lana', 'bufanda de seda', 'chal', 'poncho',
  'pantalón corto', 'pantalón largo', 'pantalón vaquero', 'pantalón de vestir', 'pantalón de deporte'
];

// Función para verificar si el texto contiene palabras no relacionadas con comida
const tokenizer = new WordTokenizer();
export function containsNonFoodWords(text: string): boolean {
  const tokens = tokenizer.tokenize(text.toLowerCase());
  return tokens.some(token => nonFoodWords.includes(token));
}
