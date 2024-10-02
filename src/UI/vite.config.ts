import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  base: './',
  build: {
    outDir: path.resolve(__dirname, '../Client/dist'),
    emptyOutDir: true,
    assetsDir: 'assets',
  },
  resolve: {
    alias: {
      '@site': path.resolve(__dirname, 'src'),
      '@components': path.resolve(__dirname, 'src/Components'),
      '@assets': path.resolve(__dirname, 'src/Assets'),
      '@constants': path.resolve(__dirname, 'src/Constants'),
      '@hooks': path.resolve(__dirname, 'src/Hooks'),
    },
  },
});
