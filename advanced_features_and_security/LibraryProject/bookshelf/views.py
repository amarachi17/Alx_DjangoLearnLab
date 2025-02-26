from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Document
from .forms

# Create your views here.
@permission_required("relationship_app.can_view", raise_exception=True)
def view_document(request, doc_id):
    document = get_object_or_404(Document, id=doc_id)
    return render(request, "document_detail.html", {"document": document})

@permission_required("relationship_app.can_create", raise_exception=True)
def create_document(request):
    # Logic to create a new document
    pass

@permission_required("relationship_app.can_edit", raise_exception=True)
def edit_document(request, doc_id):
    # Logic to create a new document
    pass

@permission_required("relationship_app.can_delete", raise_exception=True)
def delete_document(request, doc_id):
    # Logic to create a new document
    pass
