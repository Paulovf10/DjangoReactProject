from enum import Enum


class EnumTipoUsuario(Enum):
    ADMINISTRADOR = 1
    GESTOR = 2
    COLABORADOR = 3


class EnumTipoMeta(Enum):
    COLABORADOR = 1
    EQUIPE = 2
