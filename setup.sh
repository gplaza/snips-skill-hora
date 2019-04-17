#/usr/bin/env bash -e


# ===================
# DEFINIMOS VARIABLES
# ===================
VENV=venv
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

# =========================
# CREAMOS ENTORNO VIRTUAL
# =========================
printf "Creamos entorno virtual ...\t"
if [ ! -d "$VENV" ]
then
    PYTHON=`which python3`
    if [ ! -f $PYTHON ]
    then
        echo "Could not find python3"
    fi
    virtualenv -p $PYTHON $VENV
fi
printf "OK\n"

# =========================
# ACTIVAMOS ENTORNO VIRTUAL
# =========================
printf "Activamos entorno virtual ...\t"
. $VENV/bin/activate
printf "OK\n"

# =================================
# INSTALAMOS DEPENDENCIAS DE PYTHON
# =================================
printf "Instalamos dependencias de Python ...\t"
pip install -r requirements.txt > /dev/null 2>&1
printf "OK\n"

# ==================
# ASIGNAMOS PERMISOS
# ==================
printf "Asignamos permisos al Skill ...\t"
sudo chmod -R 775 $SCRIPTPATH
sudo chown -R _snips-skills:_snips-skills $SCRIPTPATH
printf "OK\n"
