from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse
from .forms import UploadFileForm
from .models import file, SharedFile
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from cryptography.fernet import Fernet
from django.contrib.auth.models import User
from django.http import JsonResponse


def generate_and_load_key():
    """
    Generates a key for encryption and returns it.

    Returns:
        The generated or loaded key
    """
    key = Fernet.generate_key()
    with open("fileshare\secret.key", "wb") as file:
        file.write(key)
    return open("fileshare\secret.key", "rb").read()


def encrypt_file(key, plaintext):
    """
    Encrypts the given plaintext using the provided key.

    Args:
        The encryption key
        Plaintext:The data to be encrypted.

    Returns:
        The encrypted data.
    """
    f = Fernet(key)
    encrypted_data = f.encrypt(plaintext)
    return encrypted_data


def decrypt_file(key, ciphertext):
    """
    Decrypts the given ciphertext using the provided key.

    Args:
        The decryption key.
        Ciphertext:The data to be decrypted.

    Returns:
        str: The decrypted data as a string.
    """
    f = Fernet(key)
    decrypted_data = f.decrypt(ciphertext).decode('ascii')
    return decrypted_data


@login_required
def home(request):
    """
    Handles the home view, allowing users to upload and view their files.

    Returns:
        HttpResponse: Rendered HTML response for the home page.
    """
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        file_field = request.FILES.get("document", None)
        if file_field is not None:
            # Generates or loads the key
            key1 = generate_and_load_key()

            encrypted_data = encrypt_file(key1, file_field.read())

            with file_field.open(mode='wb') as encrypted_file:
                encrypted_file.write(encrypted_data)

                # Createa a file entry in the database
                documents = file.objects.create(
                    tittle=file_field.name, document=encrypted_file, user=request.user, key=key1)
            return HttpResponse(f"Succesfully uploaded file: {documents.tittle}")
    else:
        form = UploadFileForm()

    # Gets the document belonging to the current user
    document_file = file.objects.filter(user=request.user)
    return render(request, "home.html", {"document_file": document_file, "forms": form})


@login_required
def download_file(request, file_id):
    """
    Handles the download view for a specific file.

    Args:
        The HTTP request.
        The ID of the file to download.

    Returns:
        HttpResponse: Rendered HTML response for the download page.
    """
    document = get_object_or_404(file, id=file_id)

    # Checks if the user logged in matches
    # the user that owns the document
    if request.user != document.user:
        raise PermissionDenied

    # Decrypts the file content
    decrypted_data = decrypt_file(document.key, document.document.read())

    # Creates a response with the decrypted content
    response = FileResponse(
        decrypted_data, content_type='application/force-download')

    # Sets the appropriate Content-Disposition header for download
    response['Content-Disposition'] = f'attachment; filename={document.tittle}'

    return response


@login_required
def share_file(request, file_id):
    document = get_object_or_404(file, id=file_id, user=request.user)

    # Check if the user has permission to share this file
    if request.user != document.user:
        raise PermissionDenied

    if request.method == 'POST':
        shared_with_user_id = request.POST.get('shared_with_user')
        shared_with_user = get_object_or_404(User, id=shared_with_user_id)

        # Create a SharedFile entry
        shared_file = SharedFile.objects.create(
            file=document, shared_by=request.user, shared_with=shared_with_user)

        return JsonResponse({'message': f"File '{document.tittle}' shared with {shared_with_user.username}"})
    else:
        users = User.objects.all()
        return render(request, 'share_file.html', {'document': document, 'users': users})


@login_required
def shared_file_list(request):
    """
    Displays a list of files shared with the current user.

    Args:
        The HTTP request.

    Returns:
        HttpResponse: Rendered HTML response for the shared file list.
    """
    # Gets the currently logged-in user
    current_user = request.user

    # Gets the shared files for the current user
    shared_files = SharedFile.objects.filter(shared_with=current_user)

    context = {'user': current_user, 'shared_files': shared_files}
    return render(request, 'list.html', context)
