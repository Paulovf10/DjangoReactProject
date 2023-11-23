from core.constants import EnumTipoUsuario, EnumTipoMeta, EnumUnidadeMedida, EnumTipoNota

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

TIPO_NOTA = (
    (EnumTipoNota.S.value, 'S'),
    (EnumTipoNota.A.value, 'A'),
    (EnumTipoNota.B.value, 'B'),
    (EnumTipoNota.C.value, 'C'),
    (EnumTipoNota.D.value, 'D'),
    (EnumTipoNota.F.value, 'E'),
)