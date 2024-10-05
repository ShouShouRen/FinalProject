import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import vitePluginImp from 'vite-plugin-imp';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    vitePluginImp({
      libList: [
        {
          libName: 'antd',
          style(name) {
            return `antd/es/${name}/style/index.js`;
          },
        },
      ],
    }),
  ],

  base: './',
  build: {
    outDir: path.resolve(__dirname, '../Client/dist'),
    emptyOutDir: true,
    assetsDir: 'assets',
    chunkSizeWarningLimit: 1000,
    rollupOptions: {
      output: {
        manualChunks: {
          antd: ['antd'],
        },
      },
    },
  },
  resolve: {
    alias: {
      '@site': path.resolve(__dirname, 'src'),
      '@components': path.resolve(__dirname, 'src/Components'),
      '@assets': path.resolve(__dirname, 'src/Assets'),
      '@constants': path.resolve(__dirname, 'src/Constants'),
      '@hooks': path.resolve(__dirname, 'src/Hooks'),
      '^~': '',
    },
  },
  css: {
    preprocessorOptions: {
      less: {
        javascriptEnabled: true,
      },
    },
  },
});
