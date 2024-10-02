import React from 'react';

interface SettingsModalProps {
  isOpen: boolean;
  title: string;
  onClose: () => void;
  Connect: () => void;
  children: React.ReactNode; // 接受 children 作為一個 prop
}

const SettingsModal: React.FC<SettingsModalProps> = ({
  isOpen,
  title,
  onClose,
  Connect,
  children,
}) => {
  if (!isOpen) return null;

  return (
    <div className='fixed inset-0 flex items-center justify-center bg-black bg-opacity-50'>
      <div className='p-5 bg-white rounded-lg shadow-lg'>
        <h2 className='mb-4 text-xl font-semibold'>{title}</h2>
        {children}
        <div className='flex justify-end mt-4'>
          <button
            className='px-3 py-1 mr-2 text-sm text-white bg-red-500 rounded hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500'
            onClick={onClose}
          >
            取消
          </button>
          <button
            className='px-3 py-1 text-sm text-white rounded bg-cyan-600 hover:bg-cyan-700 focus:outline-none focus:ring-2 focus:ring-cyan-500'
            onClick={() => {
              Connect();
              onClose();
            }}
          >
            確定
          </button>
        </div>
      </div>
    </div>
  );
};

export default SettingsModal;
