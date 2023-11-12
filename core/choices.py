from core.constants import EnumTipoUsuario, EnumTipoMeta, EnumUnidadeMedida

TIPO_USUARIO = (
    (EnumTipoUsuario.ADMINISTRADOR.value, u'Administrador'),
    (EnumTipoUsuario.GESTOR.value, u'Gestor'),
    (EnumTipoUsuario.COLABORADOR.value, u'Colaborador'),
)


TIPO_META = (
    (EnumTipoMeta.COLABORADOR.value, u'Colaborador'),
    (EnumTipoMeta.EQUIPE.value, u'Equipe'),

)


UNIDADE_MEDIDA_CHOICES = (
    (EnumUnidadeMedida.UNIDADES.value, 'Unidades'),
    (EnumUnidadeMedida.REAIS.value, 'Reais'),
    (EnumUnidadeMedida.PORCENTAGEM.value, 'Porcentagem'),
    (EnumUnidadeMedida.HORAS.value, 'Horas'),
    (EnumUnidadeMedida.DIAS.value, 'Dias'),
    (EnumUnidadeMedida.PROJETOS.value, 'Projetos'),
)