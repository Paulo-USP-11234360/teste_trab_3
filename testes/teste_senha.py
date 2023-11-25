from ..scripts.senha import check_password, hash_password

# Define uma função de teste chamada test_verificar_senha
def test_verificar_senha():
    # Cria uma variável chamada stored_password e atribui um valor fictício a ela
    stored_password = "senha123"
    
    # Calcula a senha hash usando a função hash_password
    stored_hashed_password = hash_password(stored_password)
    
    # Testa se a função check_password retorna True para a senha correta
    assert check_password("senha_correta", stored_hashed_password) is True, "A senha correta deveria ser validada"
    
    # Testa se a função check_password retorna False para uma senha incorreta
    assert check_password("senha_incorreta", stored_hashed_password) is False, "A senha incorreta deveria falhar"
