from enum import Enum


class EnumTipoUsuario(Enum):
    ADMINISTRADOR = 1
    GESTOR = 2
    COLABORADOR = 3


class EnumTipoMeta(Enum):
    COLABORADOR = 1
    EQUIPE = 2


class EnumUnidadeMedida(Enum):
    UNIDADES = 1
    REAIS = 2
    PORCENTAGEM = 3
    HORAS = 4
    DIAS = 5
    PROJETOS = 6


class EnumTipoNota(Enum):
    S = 1
    A = 2
    B = 3
    C = 4
    D = 5
    F = 6
