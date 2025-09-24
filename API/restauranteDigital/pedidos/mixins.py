import time
from rest_framework.response import Response

class ResponseTimeMixin:
    """
    Mixin que calcula e imprime o tempo de resposta de uma view.
    Conceito: DRY (Don't Repeat Yourself).
    """
    def dispatch(self, request, *args, **kwargs):
        start_time = time.time()
        response = super().dispatch(request, *args, **kwargs)
        duration = time.time() - start_time
        print(f"[INFO] View '{self.__class__.__name__}' executada em {duration:.4f} segundos.")
        return response

