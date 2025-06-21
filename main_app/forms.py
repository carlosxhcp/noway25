from allauth.account.forms import SignupForm
from django import forms
from .models import Profile
import base64
import uuid
from supabase import create_client

# Configure com seus dados reais
SUPABASE_URL = "https://kxtlacebeybfggufdsjq.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt4dGxhY2ViZXliZmdndWZkc2pxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NDMwMjc3MCwiZXhwIjoyMDU5ODc4NzcwfQ.T_Ze5gdFjKrOFH5bCCX0OOxuGn_3ocmVIsBOMw9UO_8"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class CustomSignupForm(SignupForm):
    avatar_data = forms.CharField(widget=forms.HiddenInput(), required=False)

    def save(self, request):
        user = super().save(request)
        avatar_data = self.cleaned_data.get('avatar_data')
        if avatar_data:
            format, imgstr = avatar_data.split(';base64,')
            ext = format.split('/')[-1]
            filename = f"{user.username}_{uuid.uuid4()}.{ext}"
            file_content = base64.b64decode(imgstr)

            response = supabase.storage.from_("avatars").upload(filename, file_content, {
                "content-type": f"image/{ext}"
            })

            if response.get("error"):
                print("Erro ao fazer upload no Supabase:", response["error"])
            else:
                avatar_url = f"{SUPABASE_URL}/storage/v1/object/public/avatars/{filename}"
                profile = Profile.objects.get(user=user)
                profile.avatar = avatar_url
                profile.save()

        return user
