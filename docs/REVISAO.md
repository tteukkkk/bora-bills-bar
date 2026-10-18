# Revisão para portfólio

## Alterações comuns

- Removidos ambientes virtuais, arquivos compilados, bancos SQLite, uploads locais e estáticos coletados.
- Configuração de credenciais por variáveis de ambiente; arquivo `.env.example` sem senha real.
- SQLite como padrão para demonstração e MySQL opcional.
- Dependências e instruções de instalação documentadas.
- DEFAULT_AUTO_FIELD alinhado às migrações existentes.

## Alterações específicas

Timeout e fallback para falhas nas APIs de bebidas e personagens; lista vazia de personagens não causa erro; coordenadas zero são aceitas na consulta do clima.

## Verificação executada

Python 3.12.14 / Django 5.2.18 / SQLite. 2 testes passaram; check, conferência de migrações e migrate concluíram com sucesso. Testes novos cobrem fluxos alterados e se somam aos testes originais. Não houve teste de MySQL, concorrência real, implantação ou inspeção visual em navegador da aplicação local.

## Limitações

As APIs foram simuladas nos testes; sua disponibilidade real e seus dados não foram validados. O ranking consulta personagens por cliente e pode ficar lento com muitos registros. Pontos são cadastrados manualmente; não existe motor automático de fidelidade.

## Modelos principais

- `Cliente`
