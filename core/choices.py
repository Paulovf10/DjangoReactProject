from core.constants import EnumTipoUsuario, EnumTipoMeta


TIPO_USUARIO = (
    (EnumTipoUsuario.ADMINISTRADOR.value, u'Administrador'),
    (EnumTipoUsuario.GESTOR.value, u'Gestor'),
    (EnumTipoUsuario.COLABORADOR.value, u'Colaborador'),
)


TIPO_META = (
    (EnumTipoMeta.COLABORADOR.value, u'Colaborador'),
    (EnumTipoMeta.EQUIPE, u'Equipe'),

)
