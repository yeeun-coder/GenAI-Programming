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
6. GPT_Streamlit_FunctionCall.py -> 입력: streamlit run "주소.py"

### Chapter_08
1. Stock_yfinance.ipynb
2. GPT_Multiple_Function.py
> pip install tabulate
3. STOCK_Streamlit_FunctionCall.py
> streamlit run STOCK_Streamlit_FunctionCall.py

### Chapter_09
1. LangChain_Chatbot.ipynb -> 기억 못함
2. LangChain_MultiTurn.py -> 정보를 넣어도 기억 못함
3. LangChain_Messagehistory.ipynb -> 각 id별로 각각 기억함
4. LangChain_RunableType.ipynb
5. LanChain_LCEL.ipynb
6. LangChain_Pydantic.ipynb
7. Langchain_Practice_02.ipynb : 귀여운 여인으로 바꾸기

### Chapter_10
1. Agent_Basic.ipynb
2. LangChain_Tool.ipynb
3. LangChain_ToolREPL.ipynb
https://app.tavily.com/ -> TAVILY_API_KEY 가져오기
4. LangChain_TavilySearchResult.ipynb
5. LangChain_TavilySearch.ipynb
6. LangChain_DallE.ipynb -> 이미지 출력
7. LangChain_GoogleNewsTool.ipynb
8. LangChain_CustomTool.ipynb
9. LangChain_AI_Agent.ipynb
10. LangChain_Pydantic.ipynb
11. LangChain_Tool_Stream.ipynb
12. LangChain_Chatbot_Streamlit.py

?? langchain_simple_chat_streamlit.py
과제 - 1. Langchain_Chatbot_with_Memory.py, 2. LangChain_Chatbot_Streamlit_Tool.py


### Chapter_11
연속되게 실행
1. load_data.py
2. clean_data.py
3. prepare_data.py
4. split_text.py
5. load_data.py
6. create_embeddings.py
7. store_faiss.py
8. retrieve_faiss.py
9. generate_answer.py
10. main.py
<img width="784" height="437" alt="스크린샷 2026-11-17 오후 2 55 07" src="https://github.com/user-attachments/assets/6af96863-f8df-4289-a0aa-15dc2decf982" />


### Chapter_12
1. RAG_Practice_01.ipynb
2. RAG_Retriever.py
3. RAG_Chat_Streamlit_01.py
4. RAG_Chat_Streamlit.py
<img width="811" height="748" alt="스크린샷 2026-11-24 오후 3 34 14" src="https://github.com/user-attachments/assets/33dcd306-6701-42b3-8a59-926b61fa814d" />


### Chapter_13
1. AI_Agent_DuckDuckGo.ipynb








