from app.extensions import db
from app.models import Categoria

def listar_todas_categorias():
    return Categoria.query.order_by(Categoria.id.desc()).all()


def obter_categoria(categoria_id):
    return Categoria.query.get_or_404(categoria_id)