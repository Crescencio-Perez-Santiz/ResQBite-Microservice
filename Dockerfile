FROM node:20

WORKDIR /app

# Copia el archivo package.json y package-lock.json al contenedor
COPY package.json package-lock.json ./

# Instala las dependencias del proyecto
RUN npm install

# Copia el resto del código de la aplicación al contenedor
COPY . .

# Compila el proyecto TypeScript
RUN npm run build

# Expone el puerto en el que la aplicación estará escuchando
EXPOSE 3000

# Define el comando de inicio de la aplicación en modo desarrollo
CMD ["npm", "run", "dev"]
