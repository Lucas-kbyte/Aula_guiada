from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.models import Usuario


def listar_todos_usuarios():
    return Usuario.query.order_by(Usuario.id.desc()).all()


def obter_usuario(usuario_id):
    return Usuario.query.get_or_404(usuario_id)

def salvar_usuario(nome, email, senha=None, usuarios_id=None):
    if not nome or not email:
        return False, "Nome e email são obrigatórios :/"
    
    try:
        if usuarios_id:
            usuario = obter_usuario(usuarios_id)
            usuario.nome = nome
            usuario.email = email
            
            if senha and senha.strip():
                usuario.set_senha(senha)
                
            mensagem = "Usuário atualizado com sucesso :3"
            
        else:
            if not senha:
                return False, "Senha é obrigatória para novos usuários :/"
            
            usuario = Usuario(nome=nome, email=email)
            usuario.set_senha(senha)
            
            db.session.add(usuario)
            mensagem = "Usuário cadastrado com sucesso :3"
            
        db.session.commit()
        return True, mensagem
    
    except IntegrityError:
        db.session.rollback()
        return False, "Erro: Email já cadastrado :/"
    
    except Exception as e:
        db.session.rollback()
        return False, f"Erro interno: {str(e)}"
    
def excluir_usuario(usuario_id):
    usuario = obter_usuario(usuario_id)
    
    try:
        db.session.delete(usuario)
        db.session.commit()
        return True, "Usuário excluído com sucesso :3"
    
    except Exception as e:
        db.session.rollback()
        return False, f"Erro ao excluir o usuário: {str(e)}"
