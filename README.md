# Generative-AI-Programming

## LLM 설정하기
* Create Virtual Environment
  * python –m venv venvPython312x

* Activate Virtual Environment
  * window : .\venvPython312x\Scripts\activate
  * mac : source venvPython312x/bin/activate

* project click -> Show and Run Commands -> Python: Select Interpreter -> Python 3.1x.xx (venvPython312x)

## StreamIit 실습 해보기
1. https://streamlit.io
2. 'Try the live playground!' click
3. 'LLM chat' click
4. > pip install streamlit 입력  (터미널 -> <)
5. > streamlit hello 입력 -> http://localhost:8501
6. Chapter_04_SourceCode Streamlit_Basic.py coding
7. > streamlit run Streamlit_Basic.py -> Streamlit에서 인공지능 사용 가능

## 실습 설명
### Chapter_04
* Streamlit_Basic.py : streamlit 실습
* PDFfile_Text.py : KSCI_Paper.pdf -> KSCI_Paper.txt
* PDFfile_Preprocessing.py : KSCI_Paper.pdf -> KSCI_Paper_with_Preprocessing.txt
* Text_Summary.py : KSCI_Paper_with_Preprocessing.txt -> Paper_summary.txt
* PDF_Summary.py : KSCI_Paper.pdf -> PDF_Paper_summary.txt

### Chapter_05
> pip3 install torch torchvision torchaudio
> brew install ffmpeg
* STT_Whisper.ipynb -> STT_Audio_Chunks.csv -> Huggingface_whisper.ipynb
* TTS_JSON_Speech.ipynb -> LLM_TTS_Sample.mp3
* LLM_TTS.ipynb -> LLM_TTS_Sample_ash.mp3, LLM_TTS_Sample_nova.mp3

### Chapter_06
1. Image_description.ipynb
2. Image_Analyzer.ipynb
3. Image_Quiz.ipynb
4. Image_Quiz_01.ipynb -> Image_quiz.md
5. Image_Quiz_Eng.ipynb -> Image_quiz.md
6. Image_Quiz_EngListening.ipynb -> Image_Quiz_Eng.md
7. TTS_JSON_Speech.ipynb -> Eng_Listening_1.mp3, Eng_Listening_2.mp3

### Chapter_07
1. GPT_Date_Function.py -> ex) 2026-10-06 13:58:44
2. GPT_FunctionCall.py
> User    :  Hi
> 
> ChatCompletionMessage(content='Hello! How can I assist you today?', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None, annotations=[])
> 
> AI      : Hello! How can I assist you today?
> 
> User    : 지금 몇 시인지 알려줘!
> 
> ChatCompletionMessage(content=None, refusal=None, role='assistant', audio=None, function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_iKOljOgD9GOUTqK33HzUIK9z', function=Function(arguments='{}', name='get_current_time'), type='function')], annotations=[])
> 2026-10-06 14:01:52
> 
> AI      : 현재 시간은 2026년 10월 6일 오후 2시 1분입니다.
> 
> User    :  exit
3. GPT_Timezone_Function.py
> 2026-10-06 01:13:28 America/New_York
4. GPT_Timezone_FunctionCall.py
> User    : 현재 시간 알려줘  
> AI      : 어느 지역의 시간을 알고 싶으신가요? 예를 들어, 서울의 시간을 알고 싶다면 "Asia/Seoul"과 같이 말씀해 주세요.  
> User    : 서울  
> 2026-10-06 14:17:23 Asia/Seoul   
> AI      : 서울의 현재 시간은 2026년 10월 6일 오후 2시 17분입니다.  
> User    : 런던  
> 2026-10-06 06:17:37 Europe/London  
> AI      : 런던의 현재 시간은 2026년 10월 6일 오전 6시 17분입니다.  
> User    : 비슈케크   
> 2026-10-06 11:18:29 Asia/Bishkek  
> AI      : 비슈케크의 현재 시간은 2026년 10월 6일 오전 11시 18분입니다.  
> User    : exit
5. GPT_MultiTimezone_FunctionCall.py
> User    : 서울, 런던, 비슈케는 몇 시야?
> 
> 2026-10-06 14:23:29 Asia/Seoul  
> 2026-10-06 06:23:29 Europe/London  
> 2026-10-06 11:23:29 Asia/Bishkek
> 
> AI      : 현재 시간은 다음과 같습니다:
> 
> - 서울: 2026년 10월 6일 오후 2시 23분
> - 런던: 2026년 10월 6일 오전 6시 23분
> - 비슈케크: 2026년 10월 6일 오전 11시 23분
> 
> User    : exit
