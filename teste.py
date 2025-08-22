
#USA ISSO PARA ENTENDER MELHOR COMO AS COISAS ESTÃO FUNCIONANDO NAS CLASSES

import psycopg2

def conectar_ao_banco():
    try:
        conn = psycopg2.connect(
            host="localhost",
            port=5433,
            database="barbearia",
            user="postgres",
            password="senha"
        )
        print("Conexão bem-sucedida!")
        return conn
    
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
    
def criar_cliente(nome, email, cpf, endereco, numero_celular):
    conn = conectar_ao_banco()
    if not conn:
        print("Problemas ao conectar-se ao banco de dados!")
        return
    try:
        with conn.cursor() as cur: 

            cur.execute("SELECT 1 FROM cliente WHERE cpf = %s", (cpf,))
            resultado = cur.fetchone()
            if not resultado:
                cur.execute(
                    "INSERT INTO cliente(nome, email, cpf, endereco, numero_celular) VALUES(%s,%s,%s,%s,%s)", 
                    (nome,email, cpf, endereco, numero_celular)
                    )  
                conn.commit()
            else:
                 print("Usuário já cadastrado")

    except Exception as e:
            print("Erro ao adicionar cliente:", e)
            conn.rollback()            #DESFAZ TODAS AS ALTERAÇÕES FEITAS NA TRANSAÇÃO ATUAL
    finally:
            conn.close()

def ler_clientes():
    conn = conectar_ao_banco()
    if not conn:
        print("Problemas ao conectar-se ao banco de dados!")
        return
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM cliente ORDER BY idcliente")
            clientes = cur.fetchall()
        return clientes
        
    except Exception as e:
            print("Erro ao listar clientes:", e)
    finally:
            conn.close()

def atualizar_cliente(coluna_alterada, chave_cliente, novo_dado):
    colunas_permitidas = ['nome', 'email', 'endereco', 'numero_celular']
    conn = conectar_ao_banco()
    if not conn:
        print("Problemas ao conectar-se ao banco de dados!")
        return
    
    if coluna_alterada not in colunas_permitidas:
        print(f"Não é possível alterar a coluna: {coluna_alterada}")
        return
    try:
        with conn.cursor() as cur:
            query = f"UPDATE cliente SET {coluna_alterada} = %s WHERE cpf = %s"
            cur.execute(query, (novo_dado, chave_cliente))
            conn.commit()
            
            if cur.rowcount == 0:
                print("CPF não encontrado. Nenhum cliente atualizado.")
            else:
                print("Cliente atualizado com sucesso!")

    except Exception as e:
            print("Erro ao atualizar cliente:", e)
    finally:
            conn.close()
             
def remover_cliente(chave_cliente):     #DECIDIR SE A CHAVE DO CLIENTE VAI SER CPF OU NÃO
    conn = conectar_ao_banco()
    if not conn:
        print("Problemas ao conectar-se ao banco de dados!")
        return
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM cliente where = %s", (chave_cliente,))
            conn.commit()

    except Exception as e:
            print("Erro ao deletar cliente:", e)
    finally:
            conn.close()    

#cadastrar_agendamento()

#cancelar_agendamento()

#atualizar_agendamento()

#cadastrar_pagamento()

#estornar_pagamento()

#cadastrar_funcionario()

#atualizar_funcionario()

#remover_funcionario()

def main():
    
    criar_cliente("João Silva", "joao.silva@email.com", "12345678901", "Rua A, 101", "999999001")
    criar_cliente("Maria Oliveira", "maria.oliveira@email.com", "12345678902", "Rua B, 202", "999999002")
    criar_cliente("Pedro Santos", "pedro.santos@email.com", "12345678903", "Rua C, 303", "999999003")
    criar_cliente("Ana Costa", "ana.costa@email.com", "12345678904", "Rua D, 404", "999999004")
    criar_cliente("Lucas Pereira", "lucas.pereira@email.com", "12345678905", "Rua E, 505", "999999005")
    criar_cliente("Carolina Almeida", "carolina.almeida@email.com", "12345678906", "Rua F, 606", "999999006")
    criar_cliente("Felipe Souza", "felipe.souza@email.com", "12345678907", "Rua G, 707", "999999007")
    criar_cliente("Beatriz Lima", "beatriz.lima@email.com", "12345678908", "Rua H, 808", "999999008")
    criar_cliente("Rafael Rocha", "rafael.rocha@email.com", "12345678909", "Rua I, 909", "999999009")
    criar_cliente("Juliana Martins", "juliana.martins@email.com", "12345678910", "Rua J, 1010", "999999010")
    criar_cliente("Thiago Fernandes", "thiago.fernandes@email.com", "12345678911", "Rua K, 1111", "999999011")
    criar_cliente("Patrícia Gomes", "patricia.gomes@email.com", "12345678912", "Rua L, 1212", "999999012")
    criar_cliente("Gabriel Santos", "gabriel.santos@email.com", "12345678913", "Rua M, 1313", "999999013")
    criar_cliente("Fernanda Ribeiro", "fernanda.ribeiro@email.com", "12345678914", "Rua N, 1414", "999999014")
    criar_cliente("Vinícius Lima", "vinicius.lima@email.com", "12345678915", "Rua O, 1515", "999999015")
    criar_cliente("Aline Souza", "aline.souza@email.com", "12345678916", "Rua P, 1616", "999999016")
    criar_cliente("Eduardo Costa", "eduardo.costa@email.com", "12345678917", "Rua Q, 1717", "999999017")
    criar_cliente("Larissa Oliveira", "larissa.oliveira@email.com", "12345678918", "Rua R, 1818", "999999018")
    criar_cliente("Bruno Martins", "bruno.martins@email.com", "12345678919", "Rua S, 1919", "999999019")
    criar_cliente("Camila Rocha", "camila.rocha@email.com", "12345678920", "Rua T, 2020", "999999020") 

    clientes = ler_clientes()
    for n in clientes:
        print(n)
    
    atualizar_cliente('nome', '12345678901', 'antonio')

    clientes = ler_clientes()
    print(clientes)


if __name__ == "__main__":
    main()
    