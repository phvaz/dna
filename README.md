# DNA Profiling Project #

Este é um projeto em Python chamado "dna.py" que implementa um programa para identificar a quem uma sequência de DNA pertence. O programa utiliza um arquivo CSV com contagens de STRs (Short Tandem Repeats) para uma lista de indivíduos e um arquivo de texto contendo a sequência de DNA a ser analisada.
Como funciona

O programa lê o arquivo CSV contendo os dados dos indivíduos, bem como a sequência de DNA fornecida no arquivo de texto. Em seguida, realiza o cálculo da maior sequência consecutiva de repetições para cada STR presente na sequência de DNA. Comparando essas contagens com o banco de dados genético, o programa identifica o provável dono da sequência de DNA.


## Como usar ##

    Clone ou faça o download do repositório para o seu computador.
    Certifique-se de que o arquivo "dna.py", o arquivo CSV com as contagens de STRs e o arquivo de texto com a sequência de DNA estejam na mesma pasta.
    Abra um terminal ou prompt de comando na pasta onde estão os arquivos.
    Execute o programa com o seguinte comando:

    python dna.py database.csv sequence.txt

    (Substitua "database.csv" pelo nome do arquivo CSV e "sequence.txt" pelo nome do arquivo de texto com a sequência de DNA a ser analisada.)

## Resultado ##

O programa exibirá o nome do indivíduo correspondente à sequência de DNA ou "Sem correspondência" caso não haja uma correspondência exata nos dados do banco de dados genético.

Divirta-se desvendando os mistérios ocultos no DNA com esta ferramenta de genética forense poderosa!
