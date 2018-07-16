unsigned int fibonaci(unsigned int n) {
  unsigned int n_1 = 1, n_2 = 0, curr;

  if (n == 0)
    return 0;
  else if (n == 1)
    return 1;

  for (int i = 2; i <= n; i++) {
    curr = n_1 + n_2;

    n_2 = n_1;
    n_1 = curr;
  }

  return curr;
}
