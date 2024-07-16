// test/integration/app.test.ts
import request from 'supertest';
import app from './src/app'  // Ajusta la ruta según la estructura de tu proyecto

describe('GET /payments', () => {
  it('responds with 200 and returns a list of payments', async () => {
    const response = await request(app).get('/payments');
    
    expect(response.status).toBe(200);
    expect(Array.isArray(response.body)).toBe(true);  // Verifica que la respuesta sea un array de pagos (o lo que sea que esperes)
    // Aquí puedes agregar más expectativas según el formato de respuesta esperado
  });

});