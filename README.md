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
