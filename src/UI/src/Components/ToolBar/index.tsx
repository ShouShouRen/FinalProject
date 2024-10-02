import {
  RiInformation2Fill,
  RiIndentIncrease,
  RiIndentDecrease,
  RiArrowLeftRightFill,
  RiServerFill,
} from 'react-icons/ri';
import { TfiReload } from 'react-icons/tfi';
import { GiCancel } from 'react-icons/gi';
import { TbPlugConnected, TbPlugConnectedX } from 'react-icons/tb';
const ToolBar = () => {
  const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
    const title = e.currentTarget.getAttribute('title');
    console.log(`Button clicked: ${title}`);
  };
  return (
    <div className='flex flex-row items-center space-x-5 bg-gray-500 border border-white'>
      <div className='flex items-center'>
        <button title='站台管理員' onClick={handleClick}>
          <RiServerFill className='w-12 h-12 lg:w-20 lg:h-20 md:w-16 md:h-16' color='#87A2FF' />
        </button>
      </div>
      <div className='flex items-center gap-1'>
        <button title='連線紀錄' onClick={handleClick}>
          <RiInformation2Fill
            className='w-12 h-12 lg:w-20 lg:h-20 md:w-16 md:h-16'
            color='#ffc800'
          />
        </button>
        <button title='切換本地目錄樹' onClick={handleClick}>
          <RiIndentDecrease className='w-12 h-12 lg:w-20 lg:h-20 md:w-16 md:h-16' color='#7acf6a' />
        </button>
        <button title='切換遠端目錄樹' onClick={handleClick}>
          <RiIndentIncrease className='w-12 h-12 lg:w-20 lg:h-20 md:w-16 md:h-16' color='#87A2FF' />
        </button>
        <button title='檔案傳輸過程' onClick={handleClick}>
          <RiArrowLeftRightFill
            className='w-12 h-12 lg:w-20 lg:h-20 md:w-16 md:h-16'
            color='#5ba4a4'
          />
        </button>
      </div>
      <div className='flex items-center'>
        <button title='重新整理檔案及資料夾' onClick={handleClick}>
          <TfiReload className='h-9 w-9 lg:w-16 lg:h-16 md:w-12 md:h-12' color='#99ff99' />
        </button>
        <button title='取消檔案動作' className='ml-2 lg:ml-4 md:ml-3' onClick={handleClick}>
          <GiCancel className='w-10 h-10 lg:w-20 lg:h-20 md:w-16 md:h-16' color='#cc0000' />
        </button>
        <button title='連接伺服器' className='ml-1 md:ml-2' onClick={handleClick}>
          <TbPlugConnected className='w-10 h-10 lg:w-20 lg:h-20 md:w-16 md:h-16' color='#99ff33' />
        </button>
        <button title='中斷伺服器' className='-ml-1 md:-ml-2' onClick={handleClick}>
          <TbPlugConnectedX className='w-10 h-10 lg:w-20 lg:h-20 md:w-16 md:h-16' color='#ff6600' />
        </button>
      </div>
    </div>
  );
};

export default ToolBar;
