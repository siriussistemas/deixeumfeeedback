export function validateEmptyAndLength3(value) {
  if (!value) {
    return 'Este campo é obrigatório';
  } else if (value.length < 3) {
    return 'Este campo precisa de no mínimo 3 caracteres';
  }
  return true;
}

export function validateEmail(value) {
  if (!value) {
    return 'Este campo é obrigatório';
  } else if (!/^.+@.+$/i.test(value)) {
    return 'Email inválido';
  }
  return true;
}