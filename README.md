# kdb+ Community License

1. [Sign up with KX](https://developer.kx.com/products/kdb-x/install) and download your community license.
2. Create your local environment file:
   ```sh
   cp .env.example .env
   ```
3. Base64-encode the license and replace the placeholder in `.env`:
   ```sh
   base64 < /path/to/kc.lic | tr -d '\n'
   ```

<img width="2746" height="1436" alt="KX license sign-up page" src="https://github.com/user-attachments/assets/6107d3ed-5f82-4cad-806b-47e656972786" />

<img width="2824" height="1402" alt="KX license download page" src="https://github.com/user-attachments/assets/518a167e-7f36-4e87-a470-7013c5ed84c4" />
