"""Module providingFunction printing python version."""

import sqlite3

conn = sqlite3.connect('banco_salao')


table_cliente = """
create table if not exists cliente (
id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
nome_cliente VARCHAR(40) NOT NULL,
telefone_cliente VARCHAR(20) NOT NULL,
email_cliente VARCHAR(50) NOT NULL
);
"""
conn.execute(table_cliente)
conn.commit()

create_table_produto = """
CREATE TABLE IF NOT EXISTS produto (
id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
nome_produto VARCHAR(50) NOT NULL,
descricao_produto VARCHAR(100),
preco_produto DECIMAL(10,2) NOT NULL
);
"""
conn.execute(create_table_produto)
conn.commit()

create_table_servico = """
CREATE TABLE IF NOT EXISTS servico (
id_servico INTEGER PRIMARY KEY AUTOINCREMENT,
nome_servico VARCHAR(50) NOT NULL,
descricao_servico VARCHAR(100),
preco_servico DECIMAL(10,2) NOT NULL
);
"""
conn.execute(create_table_servico)
conn.commit()

create_table_agendamento_servico = """
CREATE TABLE IF NOT EXISTS agendamento_servico (
id_agendamento INTEGER PRIMARY KEY AUTOINCREMENT,
id_cliente INTEGER NOT NULL,
id_servico INTEGER NOT NULL,
dia_agendamento DATE NOT NULL,
hora_agendamento TIME NOT NULL,
status_agendamento VARCHAR(10) NOT NULL,
 FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente),
 FOREIGN KEY (id_servico) REFERENCES servico (id_servico)
);
"""
conn.execute(create_table_agendamento_servico)
conn.commit()

create_table_pagar_servico = """
create table if not exists pagar_servico (
id_pagamento_servico integer primary key autoincrement,
id_servico integer not null,
id_cliente integer not null,
forma_pagamento VARCHAR(20) not null,
foreign key (id_servico) references servico (id_servico),
foreign key (id_cliente) references cliente (id_cliente)
);
"""
conn.execute(create_table_pagar_servico)
conn.commit()

create_table_pagar_produto = """
create table if not exists pagar_produto (
id_pagamento_produto integer primary key autoincrement,
id_produto integer not null,
id_cliente integer not null,
forma_pagamento VARCHAR(20) not null,
foreign key (id_produto) references produto (id_produto),
foreign key (id_cliente) references cliente (id_cliente)
);
"""

lista_clientes = [
('julia didra', '98546184', 'juliadidra22@gmail.com'),
('wilza minhaque', '86986526', 'wilzaminhaque@gmail.com'),
('alessandra raissa', '997317744', 'alessandra@gmail.com'),
('joao pedro', '984562436', 'joaopedroe@gmail.com'),
('giliandra costa', '97845326', 'gicosta@gmail.com'),
('maria do carmo', '985426590', 'mcarmen@gmail.com'),
('alexandro bezerra', '978589623', 'alexbezerra@gmail.com'),
('daniela diniz', '32519403', 'danidiniz@gmail.com'),
('kamille isabel', '95169746', 'kism@gmail.com'),
('bernardo braga', '921357946', 'bernabraga@gmail.com')
]

lista_servicos = [
('Corte masculino', 'Corte para homens', 35.00),
('Corte feminino', 'Corte de cabelo estilizado para mulheres', 45.00),
('Coloração de cabelo', 'tintura completa', 80.00),
('hidratação wella', 'hidratação flex wella', 70.00),
('escova', 'escova cabelo longo', 50.00),
('Pedicure', 'Cuidado e esmaltação dos pés', 30.00),
('Design de sobrancelhas', 'Modelagem e correção das sobrancelhas', 20.00),
('realinhamento tecnico', 'progressiva fit, cabelo p', 100.00),
('botox capilar', 'botox fit, cabelo p', 80.00),
('morena iluminada', 'mechas em cabelo M', 300.00)
]

lista_produtos = [
('Shampoo', 'Shampoo wella', 129.99),
('Condicionador', 'Condicionador wella', 129.99),
('Máscara capilar', 'Máscara de tratamento fit', 100.00),
('kit tratamento', 'kit fit', 79.99),
('pulseira pandora', 'pulseira pandora versão cor verde', 159.99),
('brinco coração', 'brinco prata coração em zirconias', 79.99),
('anel coração', 'anel coração prata', 59.99),
('Óleo corporal', 'Óleo hidratante natura', 50.00),
('Creme facial', 'Creme hidratante para o rosto boticario', 70.00),
('Loção corporal', 'Loção hidratante para o corpo boticario', 90.00)
]

lista_agendamento = [
(1, 1, '2023-05-14', '09:00:00', 'Agendado'),
(2, 3, '2023-05-15', '14:30:00', 'Cancelado'),
(3, 2, '2023-05-16', '11:00:00', 'Agendado'),
(4, 1, '2023-05-17', '10:30:00', 'Agendado'),
(5, 2, '2023-05-18', '15:00:00', 'Pendente'),
(6, 1, '2023-05-19', '13:30:00', 'Agendado'),
(7, 3, '2023-05-20', '16:00:00', 'Agendado'),
(8, 2, '2023-05-21', '11:30:00', 'Cancelado'),
(9, 1, '2023-05-22', '14:00:00', 'Agendado'),
(10, 3, '2023-05-23', '12:00:00', 'Agendado')
]

lista_pagar_servico = [
(1, 1, 'Cartão Crédito'),
(2, 3, 'Dinheiro'),
(3, 2, 'Cartão Débito'),
(2, 4, 'Dinheiro'),
(1, 5, 'Cartão Crédito'),
(3, 6, 'Pix'),
(1, 7, 'Pix'),
(2, 8, 'Cartão Crédito'),
(3, 9, 'Pix'),
(1, 10, 'Cartão Débito')
]

lista_pagar_produto = [
(1, 1, 'Cartão Crédito'),
(3, 3, 'Pix'),
(2, 2, 'Cartão Débito'),
(3, 4, 'Pix'),
(1, 5, 'Cartão Crédito'),
(2, 6, 'Cartão Crédito'),
(3, 7, 'Dinheiro'),
(1, 8, 'Pix'),
(2, 9, 'Dinheiro'),
(3, 10, 'Cartão Débito')
]

dados_cliente = """
insert into cliente ( nome_cliente, telefone_cliente, email_cliente) values
('julia didra', '98546184', 'juliadidra22@gmail.com'),
('wilza minhaque', '86986526', 'wilzaminhaque@gmail.com'),
('alessandra raissa', '997317744', 'alessandra@gmail.com'),
('joao pedro', '984562436', 'joaopedroe@gmail.com'),
('giliandra costa', '97845326', 'gicosta@gmail.com'),
('maria do carmo', '985426590', 'mcarmen@gmail.com'),
('alexandro bezerra', '978589623', 'alexbezerra@gmail.com'),
('daniela diniz', '32519403', 'danidiniz@gmail.com'),
('kamille isabel', '95169746', 'kism@gmail.com'),
('bernardo braga', '921357946', 'bernabraga@gmail.com');
"""

cursor = conn.cursor()
cursor.executemany("""
    INSERT INTO clients (nome, telefone, email)
    VALUES (?,?,?)
""", lista_clientes)

conn.execute(create_table_pagar_produto)
conn.commit()
conn.close()

