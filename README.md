# financeiro

## Instalando

```
$ poetry install
```

## Executando Fava

Fava é uma interface web para os arquivos `.beancount`. Para rodar localmente, use o comando abaixo:

```
$ poetry run fava financeiro/main.beancount
```

### Como adicionar um novo extrato mensal (apenas BB)?
- [ ] Salve o arquivo do extrato no formato `.ofx` na pasta `extratos/`. Use o formato `<ano>-<mês>-bb.ofx` como nome do arquivo (exemplo: `extratos/2022-08-bb.ofx`).
- [ ] Criei um novo arquivo `.beancount` a partir do extrato com o comando abaixo (exemplo: `2022-08-bb.ofx -> 2022-08.beancount`:
  ```
  $ poetry run bean-extract config.py extratos/2022-08-bb.ofx > financeiro/2022-08.beancount
  ```
- [ ] Seguindo no arquivo `.beancount` gerado:
  - [ ] Altere a segunda linha do arquivo de `**** /caminho/até/apyb/financeiro/extratos/...` para `;; extratos/...`
  - [ ] Para cada transação:
    - [ ] Defina a conta de entrada ou de saída, dependendo da origem e destino da transação. Siga os exemplos no README.md ou use as transações passadas como guia.
    - [ ] Confirme que cada transação relacionada a eventos tenha um comprovante na pasta `Receitas` ou `Despesas` no Google Drive.
- [ ] Inclua o arquivo editado no `financeiro/main.beancount`.
- [ ] Execute o Fava localmente. A página `Editor` deve indicar qualquer erro presente no arquivo.
- [ ] Abra um PR neste repositório com as mudanças

## Referências
- [Documentação do Beancount](https://beancount.github.io/docs/)
- [Sintaxe do arquivo `.beancount`](https://beancount.github.io/docs/beancount_language_syntax.html#syntax-overview)
- [Conceitos básicos do sistema de contabilidade de duas entradas](https://gnucash.org/viewdoc.phtml?rev=4&lang=C&doc=guide)
