## Como usar?

### Fork
Forke este repositório.

### Mantendo atualizado
Se você forcou este projeto, pode manter seu projeto atualizado com este boilerplate adicionando um git remote:

```
git remote add upstream https://github.com/getzoop/python-django-base-project.git
```

Quando precisar atualizar, apenas merge do upstream:

```
git pull upstream master
```

## FAQ

### Como criar um novo app?

```
make startapp APP=zpxpto
```

### Como executo os testes?
```
make test
```

Isso subirá um banco de testes no Docker, executará os testes e finalizará tudo logo após.

### To com pressa e quero executar apenas os testes unitários (sem banco). Comofas?

```
make unittest
```

Ele subirá o container da aplicação e usará o pytest para executar **apenas** os unittests.

Pela sanidade do projeto, não crie unit tests que acessem banco! Se precisar acessar banco, crie o teste em `{app}/tests/integration/` ou `{app}/db/`.

### Como vejo o relatório de coverage?

```
make coverage-html
```
Isso deve abrir o browser com o relatório para você. Se vc preferir ver no terminal mesmo ( `¯\_(ツ)_/¯` ), execute `make coverage-shell`

### Consigo abrir um shell do Django deste projeto?

```
make shell
```

Divirta-se

### E bash?
```
make bash
```

## TO DO

- Log com grey log
- Integrar healthcheck por padrão
- Integrar linter
