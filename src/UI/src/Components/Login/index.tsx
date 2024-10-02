import { useState } from 'react';

const Login = () => {
  const [Host, setHost] = useState<string>('');
  const [Username, setUsername] = useState<string>('');
  const [Password, setPassword] = useState<string>('');
  const [Port, setPort] = useState<string>('');
  const Connect = () => {
    console.log('Host:', Host);
    console.log('Username:', Username);
    console.log('Password:', Password);
    console.log('Port:', Port);
    console.log('Connect');
  };
  return (
    <div className='flex flex-wrap items-center justify-start p-2 bg-gray-500 border border-white gap-7'>
      <div className='flex items-center'>
        <label htmlFor='host' className='mr-1 text-sm text-white whitespace-nowrap'>
          主機(H):
        </label>
        <input
          type='text'
          id='host'
          className='px-2 py-1 text-sm border border-gray-300 rounded w-28 focus:outline-none focus:ring-1 focus:ring-cyan-500'
          value={Host}
          onChange={(e) => setHost(e.target.value)}
        />
      </div>
      <div className='flex items-center'>
        <label htmlFor='username' className='mr-1 text-sm text-white whitespace-nowrap'>
          使用者名稱(U):
        </label>
        <input
          type='text'
          id='username'
          className='px-2 py-1 text-sm border border-gray-300 rounded w-28 focus:outline-none focus:ring-1 focus:ring-cyan-500'
          value={Username}
          onChange={(e) => setUsername(e.target.value)}
        />
      </div>
      <div className='flex items-center'>
        <label htmlFor='password' className='mr-1 text-sm text-white whitespace-nowrap'>
          密碼(W):
        </label>
        <input
          type='password'
          id='password'
          className='px-2 py-1 text-sm border border-gray-300 rounded w-28 focus:outline-none focus:ring-1 focus:ring-cyan-500'
          value={Password}
          onChange={(e) => setPassword(e.target.value)}
        />
      </div>
      <div className='flex items-center'>
        <label htmlFor='port' className='mr-1 text-sm text-white whitespace-nowrap'>
          連接埠(P):
        </label>
        <input
          type='number'
          id='port'
          className='w-20 px-2 py-1 text-sm border border-gray-300 rounded focus:outline-none focus:ring-1 focus:ring-cyan-500'
          value={Port}
          onChange={(e) => setPort(e.target.value)}
        />
      </div>
      <button
        className='px-3 py-1 text-sm text-white bg-blue-600 rounded hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500'
        onClick={Connect}
      >
        快速連線(Q)
      </button>
    </div>
  );
};

export default Login;

// import React, { useState } from 'react';
// import { Modal } from '@components';

// const Login = () => {
//   const [Host, setHost] = useState('');
//   const [Username, setUsername] = useState('');
//   const [Password, setPassword] = useState('');
//   const [Port, setPort] = useState('');
//   const [isModalOpen, setIsModalOpen] = useState(false);

//   const Connect = () => {
//     console.log('Host:', Host);
//     console.log('Username:', Username);
//     console.log('Password:', Password);
//     console.log('Port:', Port);
//     console.log('Connect');
//   };

//   const handlePortChange = (e: React.ChangeEvent<HTMLInputElement>) => {
//     const value = e.target.value;
//     if (/^\d*$/.test(value)) {
//       setPort(value);
//     }
//   };

//   const openModal = () => {
//     setIsModalOpen(true);
//   };

//   const closeModal = () => {
//     setIsModalOpen(false);
//   };

//   return (
//     <div className='flex flex-col items-center p-2 bg-gray-100 rounded-l gap-7'>
//       <button
//         className='px-3 py-1 text-sm text-white rounded bg-cyan-600 hover:bg-cyan-700 focus:outline-none focus:ring-2 focus:ring-cyan-500'
//         onClick={openModal}
//       >
//         打開設定視窗
//       </button>

//       <Modal isOpen={isModalOpen} title='連線主機資訊' onClose={closeModal} Connect={Connect}>
//         <div className='flex flex-wrap items-center justify-start p-2 gap-7'>
//           <div className='flex items-center'>
//             <label htmlFor='host' className='mr-1 text-sm whitespace-nowrap'>
//               主機(H):
//             </label>
//             <input
//               type='text'
//               id='host'
//               className='px-2 py-1 text-sm border border-gray-300 rounded w-28 focus:outline-none focus:ring-1 focus:ring-cyan-500'
//               value={Host}
//               onChange={(e) => setHost(e.target.value)}
//             />
//           </div>
//           <div className='flex items-center'>
//             <label htmlFor='username' className='mr-1 text-sm whitespace-nowrap'>
//               使用者名稱(U):
//             </label>
//             <input
//               type='text'
//               id='username'
//               className='px-2 py-1 text-sm border border-gray-300 rounded w-28 focus:outline-none focus:ring-1 focus:ring-cyan-500'
//               value={Username}
//               onChange={(e) => setUsername(e.target.value)}
//             />
//           </div>
//           <div className='flex items-center'>
//             <label htmlFor='password' className='mr-1 text-sm whitespace-nowrap'>
//               密碼(W):
//             </label>
//             <input
//               type='password'
//               id='password'
//               className='px-2 py-1 text-sm border border-gray-300 rounded w-28 focus:outline-none focus:ring-1 focus:ring-cyan-500'
//               value={Password}
//               onChange={(e) => setPassword(e.target.value)}
//             />
//           </div>
//           <div className='flex items-center'>
//             <label htmlFor='port' className='mr-1 text-sm whitespace-nowrap'>
//               連接埠(P):
//             </label>
//             <input
//               type='text'
//               id='port'
//               className='w-20 px-2 py-1 text-sm border border-gray-300 rounded focus:outline-none focus:ring-1 focus:ring-cyan-500'
//               value={Port}
//               onChange={handlePortChange}
//             />
//           </div>
//         </div>
//       </Modal>
//     </div>
//   );
// };

// export default Login;
