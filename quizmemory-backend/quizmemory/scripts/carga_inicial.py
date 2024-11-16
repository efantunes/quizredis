import redis
from quizmemory.config.redis_config import MyRedisSingletonPool
from quizmemory.model.question import Question
from quizmemory.service.question_service import QuestionService


question_service = QuestionService(MyRedisSingletonPool.get_instance())



##### PROFESSORES
with redis.Redis(connection_pool=MyRedisSingletonPool.get_instance()) as r:
    id_dumbledore = r.incr('professor_id_counter')
    r.hset(f'professor:{id_dumbledore}',mapping={
        "nome" : "Dumbledore"
    })
    id_snape = r.incr('professor_id_counter')
    r.hset(f'professor:{id_snape}',mapping={
        "nome" : "Snape"
    })


##### Quizzes
############# Perguntas
quizzes = []


quiz1 = [
    Question("Qual é a capital do Brasil?", "A) Brasília", "B) Rio de Janeiro", "C) São Paulo", "D) Belo Horizonte", "A"),
    Question("Qual é o maior planeta do sistema solar?", "A) Terra", "B) Marte", "C) Júpiter", "D) Saturno", "C"),
    Question("Qual é o elemento químico representado pelo símbolo O?", "A) Ouro", "B) Oxigênio", "C) Ozônio", "D) Ósmio", "B"),
    Question("Quantos continentes existem?", "A) 5", "B) 6", "C) 7", "D) 8", "C"),
    Question("Qual animal é conhecido como o 'rei da selva'?", "A) Elefante", "B) Leão", "C) Tigre", "D) Onça", "B"),
    Question("Qual é a cor primária entre as opções?", "A) Verde", "B) Azul", "C) Rosa", "D) Preto", "B"),
    Question("Quantos segundos há em um minuto?", "A) 30", "B) 60", "C) 120", "D) 90", "B"),
    Question("Quem pintou a Mona Lisa?", "A) Van Gogh", "B) Leonardo da Vinci", "C) Michelangelo", "D) Picasso", "B"),
    Question("Qual é o menor país do mundo?", "A) Mônaco", "B) Vaticano", "C) Malta", "D) Liechtenstein", "B"),
    Question("Qual é o oceano que cobre a maior área?", "A) Atlântico", "B) Índico", "C) Pacífico", "D) Ártico", "C"),
]
quizzes.append({
    'professor_num': id_snape,
    'title': 'Quiz1',
    'questions': quiz1
})

# Quiz 2
quiz2 = [
    Question("Quantos dias há em um ano bissexto?", "A) 365", "B) 366", "C) 364", "D) 367", "B"),
    Question("Qual é o idioma mais falado no mundo?", "A) Espanhol", "B) Inglês", "C) Mandarim", "D) Hindi", "C"),
    Question("Quem foi o primeiro presidente do Brasil?", "A) Getúlio Vargas", "B) Dom Pedro II", "C) Marechal Deodoro da Fonseca", "D) Juscelino Kubitschek", "C"),
    Question("Qual é o maior órgão do corpo humano?", "A) Fígado", "B) Cérebro", "C) Coração", "D) Pele", "D"),
    Question("Quantos lados tem um hexágono?", "A) 5", "B) 6", "C) 7", "D) 8", "B"),
    Question("Qual é o país conhecido como a terra do sol nascente?", "A) China", "B) Japão", "C) Coreia do Sul", "D) Tailândia", "B"),
    Question("Quem escreveu 'Dom Quixote'?", "A) Machado de Assis", "B) Miguel de Cervantes", "C) William Shakespeare", "D) Eça de Queirós", "B"),
    Question("Qual é o estado brasileiro conhecido como 'terra do acarajé'?", "A) Pernambuco", "B) Bahia", "C) Ceará", "D) Pará", "B"),
    Question("Qual é o planeta mais próximo do Sol?", "A) Vênus", "B) Mercúrio", "C) Marte", "D) Terra", "B"),
    Question("Qual é a moeda oficial do Japão?", "A) Yuan", "B) Dólar", "C) Iene", "D) Won", "C"),
]

quizzes.append({
    'professor_num': id_snape,
    'title': 'Quiz2',
    'questions': quiz2
})

quiz3 = [
    Question("Qual é o menor planeta do sistema solar?", "A) Mercúrio", "B) Marte", "C) Vênus", "D) Terra", "A"),
    Question("Quem pintou 'A Última Ceia'?", "A) Leonardo da Vinci", "B) Van Gogh", "C) Michelangelo", "D) Rembrandt", "A"),
    Question("Qual é o símbolo químico do ouro?", "A) Au", "B) Ag", "C) Fe", "D) Hg", "A"),
    Question("Qual é o país mais populoso do mundo?", "A) Índia", "B) China", "C) Estados Unidos", "D) Indonésia", "B"),
    Question("Quantos lados tem um triângulo?", "A) 2", "B) 3", "C) 4", "D) 5", "B"),
    Question("Em que continente está o Brasil?", "A) América do Norte", "B) Europa", "C) América do Sul", "D) África", "C"),
    Question("Qual instrumento mede terremotos?", "A) Barômetro", "B) Sismógrafo", "C) Termômetro", "D) Higrômetro", "B"),
    Question("Quem foi o primeiro homem a pisar na Lua?", "A) Neil Armstrong", "B) Buzz Aldrin", "C) Yuri Gagarin", "D) Michael Collins", "A"),
    Question("Qual é o maior deserto do mundo?", "A) Saara", "B) Gobi", "C) Kalahari", "D) Antártico", "D"),
    Question("Quantos graus tem um círculo?", "A) 90", "B) 180", "C) 360", "D) 270", "C"),
]
quizzes.append({
    'professor_num': id_snape,
    'title': 'Quiz3',
    'questions': quiz3
})

# Quiz 3
quiz4 = [
    Question("Em que ano ocorreu a independência do Brasil?", "A) 1820", "B) 1822", "C) 1824", "D) 1826", "B"),
    Question("Quem descobriu o Brasil?", "A) Cristóvão Colombo", "B) Vasco da Gama", "C) Pedro Álvares Cabral", "D) Fernão de Magalhães", "C"),
    Question("Qual é a montanha mais alta do mundo?", "A) K2", "B) Kangchenjunga", "C) Monte Everest", "D) Kilimanjaro", "C"),
    Question("Quantos segundos há em uma hora?", "A) 3.600", "B) 3.000", "C) 4.200", "D) 3.200", "A"),
    Question("Quem pintou 'Noite Estrelada'?", "A) Van Gogh", "B) Salvador Dalí", "C) Claude Monet", "D) Pablo Picasso", "A"),
    Question("Qual é o maior rio do mundo?", "A) Nilo", "B) Amazonas", "C) Yangtzé", "D) Mississipi", "B"),
    Question("Qual é a capital do Japão?", "A) Pequim", "B) Seul", "C) Tóquio", "D) Bangkok", "C"),
    Question("Quem escreveu 'Os Lusíadas'?", "A) Fernando Pessoa", "B) Luís de Camões", "C) Machado de Assis", "D) Eça de Queirós", "B"),
    Question("Qual país é conhecido pelo samba?", "A) Argentina", "B) Brasil", "C) México", "D) Cuba", "B"),
    Question("Quantos dentes tem um adulto?", "A) 28", "B) 30", "C) 32", "D) 36", "C"),
]
quizzes.append({
    'professor_num': id_snape,
    'title': 'Quiz4',
    'questions': quiz4
})


for quiz in quizzes:
    question_service.create_quiz_with_questions(quiz['professor_num'],quiz['title'],quiz['questions'])