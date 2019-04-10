
# Snips Skill para la hora en español
Versión 1.1

## Snips.ai
[APP](https://console.snips.ai/store/es/skill_m6K1Kv6kPbe) en la consola de Snips

## Instalación desde SAM
La forma más sencilla de instalar este Skill es mediante [Sam](https://snips.gitbook.io/getting-started/installation)

`sam install actions -g https://github.com/gplaza/snips-skill-hora.git`

## Instalación manual
- Ir a la carpeta `/var/lib/snips/skills`
- Clona este repositorio: `git clone https://github.com/gplaza/snips-skill-hora.git`
- Ejecuta el script `sh setup.sh` (esto creará el entorno virtual necesario)
- Reinicia el servicio de Skills de Snips `sudo service snips-skill-server restart`

## Configuración
Edite el fichero `config.ini` para ajustar el Skill.
Por defecto, está configurado para España.

```
[skill]
timezone: Europe/Madrid
intent_name: gplaza:askTime
```

## Lista de pendientes
- Config file in `setup.sh`
- Add instructions in `README.md`
- Multi-language
