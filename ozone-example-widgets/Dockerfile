FROM node:10.16.0-stretch

WORKDIR /app

# Install dependencies
COPY ./package.json /app
RUN npm install

# Copy application sources
COPY . /app

# Default start script
CMD ["npm", "run", "start:prod"]
