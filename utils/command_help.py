from utils import command_prefix


def get(command_name):

    name = str(command_name)

    if name is 'spoiler':
        return 'Uso: {prefix}spoiler "titulo" "texto"\n' \
               'Esconde los spoilers para que Saki no se chive.'.format(prefix=command_prefix)
    if name is 'limpiar':
        return 'Uso: {prefix}limpiar N\n' \
               'Borra los ultimos N mensajes o los que haya.'.format(prefix=command_prefix)
    else:
        return '{prefix}{name}??? De que me estas hablando maestro'.format(prefix=command_prefix, name=name)
