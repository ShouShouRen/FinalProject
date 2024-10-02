import {
  RiInformation2Fill,
  RiIndentIncrease,
  RiIndentDecrease,
  RiArrowLeftRightFill,
  RiServerFill,
} from 'react-icons/ri';
const ToolBar = () => {
  return (
    <div className='flex flex-row items-center space-x-4 bg-gray-500 border border-white'>
      <div className='flex items-center'>
        <button title='站台管理員'>
          <RiServerFill className='w-12 h-12' color='#87A2FF' />
        </button>
      </div>
      <div className='flex items-center gap-1'>
        <button title='連線紀錄'>
          <RiInformation2Fill className='w-12 h-12' color='#ffc800' />
        </button>
        <button title='切換本地目錄樹'>
          <RiIndentDecrease className='w-12 h-12' color='#7acf6a' />
        </button>
        <button title='切換遠端目錄樹'>
          <RiIndentIncrease className='w-12 h-12' color='#87A2FF' />
        </button>
        <button title='檔案傳輸過程'>
          <RiArrowLeftRightFill className='w-12 h-12' color='#5ba4a4' />
        </button>
      </div>
    </div>
  );
};

export default ToolBar;
