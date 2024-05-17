-- Habilita a extensão pgcrypto, necessária para gerar UUIDs
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Criação da tabela User
CREATE TABLE "Orders" (
    order_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_name VARCHAR(255) NOT NULL,
    user_email TEXT NOT NULL,
    description TEXT NOT NULL
);
