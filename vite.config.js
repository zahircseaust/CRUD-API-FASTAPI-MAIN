import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  server: {
    port: 5173,
    strictPort: true, // Ensures Vite doesn't switch to a different port
    hmr: {
      protocol: "ws", // Can be 'ws' or 'wss' (for secure connections)
      host: "localhost",
    },
  },
  plugins: [react()],
});
