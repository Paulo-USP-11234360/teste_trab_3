from ..scripts.senha import check_password

# Define uma função de teste chamada test_verificar_senha
def test_verificar_senha():
    # Cria uma variável chamada stored_hashed_password e atribui um valor fictício a ela
    stored_hashed_password = "senha123"  # Substitua com o valor real
    
    # Testa se a função check_password retorna True para a senha "senha_correta"
    assert check_password("senha_correta", stored_hashed_password) is True, "Validação para senha correta"
    
    # Testa se a função check_password retorna False para a senha "senha_incorreta"
    assert check_password("senha_incorreta", stored_hashed_password) is False, "Validação para senha incorreta"
