from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine
#session -> sempre que for trabalhar com banco, ele garante as transacoes
#sqlmodel -> herdamos tudo do sqlmodel

class Hero(SQLModel, table=True): #transforma toda a classe em uma tabela de um banco.
    id: Optional[int] = Field(default=None, primary_key=True) #field, quando eu quero colocar mais detalhes em uma coluna
    name: str
    secret_name: str
    age: Optional[int] = None

engine = create_engine('sqlite:///database.db', echo=True) #cria uma instancia de um banco sqlite, o echo=true eu to pedindo pra ele me mostra tudo que ta fazendo

SQLModel.metadata.create_all(engine) #contém informações sobre todas as tabelas que foram definidas no seu código usando o SQLModel. Cada classe com table=True adiciona sua estrutura ao objeto metadata.
                                     # o create_all(engine) percorre todas as tabelas registradas no metadata e cria as tabelas no banco de dados especificado pelo engine
                                     #o engine a conexao criada com o banco de dados

hero_1 = Hero(name="Deadpond", secret_name='Dive Wilson')
hero_2 = Hero(name='Spider-boy', secret_name='Pedro Parqueador')
hero_3 = Hero(name='Rusty-Man', secret_name='Tommy Sharp', age=48)

with Session(engine) as session: #Session -> gerencia a interação com o banco de dados, atuando como uma camada intermediaria entre o python e o banco, permitindo: executar consultas sql,#persistir dados no banco, controlar transações.
    session.add(hero_1)          #with -> está abrindo a sessão no inicio do bloco, após o termino do bloco ela é fechada automaticamente, evitando vazamento de recursos(como conexão abertas)
    session.add(hero_2)
    session.add(hero_3)
    session.commit()                               
                                    

