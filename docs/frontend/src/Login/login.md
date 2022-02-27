# Login

> Essa feature permite ao usuário acessar o PMS Sapron com email e senha.

## Regras

- Para acessar o sistema senha e email devem ser obrigatórios;
- O campo da senha deve por padrão ocultar o que foi digitado pelo usuário;
- Somente ao clicar no olho do campo senha a senha deve ficar visível;
- Se o campo de senha não for preenchido a mensagem “Senha obrigatória” deve ser exibida para o usuário;
- Se o usuário ou senha não forem válidos o sistema deve mostrar mensagem “Não foi possível efetuar o login”;
- Se usuário e senha estiverem corretos o usuário deve ser redirecionado para: 
  1. **Atendente**: redireciona para Página do multicalendario.
  2. **Host**: redireciona para Página de controle;
  3. **Owner**: redireciona par Página do Proprietário;


Ao clicar no botão Entrar o sistema faz um POST no endpoint:
```bash
http://localhost:8000/login/token/
```
## Onde está o código
**Backend** [aqui](https://github.com/cabfersp/sapron-pms-web/blob/main/backend/account/views.py)

**Frontend** [aqui](https://github.com/cabfersp/sapron-pms-web/blob/main/front/src/pages/Login/Login.tsx)