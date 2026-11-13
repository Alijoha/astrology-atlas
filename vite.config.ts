import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
export default defineConfig({ plugins: [react()], build: {rollupOptions: {output: {manualChunks: {astronomy: ['astronomy-engine'], vendor: ['react','react-dom','luxon']}}}} });
