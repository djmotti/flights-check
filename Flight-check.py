{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "dd1b8563-9bef-49a8-b8cd-0193707c0dcd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'cells': [{'cell_type': 'code',\n",
       "   'execution_count': None,\n",
       "   'id': '99ed954e-aa6a-4224-9f66-d95b2d965135',\n",
       "   'metadata': {},\n",
       "   'outputs': [{'name': 'stdout',\n",
       "     'output_type': 'stream',\n",
       "     'text': [\" * Serving Flask app '__main__'\\n\", ' * Debug mode: off\\n']},\n",
       "    {'name': 'stderr',\n",
       "     'output_type': 'stream',\n",
       "     'text': ['WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\\n',\n",
       "      ' * Running on http://127.0.0.1:5000\\n',\n",
       "      'Press CTRL+C to quit\\n',\n",
       "      '127.0.0.1 - - [25/Jan/2025 01:14:53] \"GET / HTTP/1.1\" 404 -\\n',\n",
       "      '127.0.0.1 - - [25/Jan/2025 01:14:53] \"GET /favicon.ico HTTP/1.1\" 404 -\\n',\n",
       "      '127.0.0.1 - - [25/Jan/2025 01:16:03] \"GET / HTTP/1.1\" 404 -\\n']}],\n",
       "   'source': ['from flask import Flask, request\\n',\n",
       "    'from twilio.twiml.messaging_response import MessagingResponse\\n',\n",
       "    'from googletrans import Translator\\n',\n",
       "    'import requests\\n']}],\n",
       " 'metadata': {'kernelspec': {'display_name': 'Python [conda env:base] *',\n",
       "   'language': 'python',\n",
       "   'name': 'conda-base-py'},\n",
       "  'language_info': {'codemirror_mode': {'name': 'ipython', 'version': 3},\n",
       "   'file_extension': '.py',\n",
       "   'mimetype': 'text/x-python',\n",
       "   'name': 'python',\n",
       "   'nbconvert_exporter': 'python',\n",
       "   'pygments_lexer': 'ipython3',\n",
       "   'version': '3.11.3'}},\n",
       " 'nbformat': 4,\n",
       " 'nbformat_minor': 5}"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "{\n",
    " \"cells\": [\n",
    "  {\n",
    "   \"cell_type\": \"code\",\n",
    "   \"execution_count\": None,\n",
    "   \"id\": \"99ed954e-aa6a-4224-9f66-d95b2d965135\",\n",
    "   \"metadata\": {},\n",
    "   \"outputs\": [\n",
    "    {\n",
    "     \"name\": \"stdout\",\n",
    "     \"output_type\": \"stream\",\n",
    "     \"text\": [\n",
    "      \" * Serving Flask app '__main__'\\n\",\n",
    "      \" * Debug mode: off\\n\"\n",
    "     ]\n",
    "    },\n",
    "    {\n",
    "     \"name\": \"stderr\",\n",
    "     \"output_type\": \"stream\",\n",
    "     \"text\": [\n",
    "      \"WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\\n\",\n",
    "      \" * Running on http://127.0.0.1:5000\\n\",\n",
    "      \"Press CTRL+C to quit\\n\",\n",
    "      \"127.0.0.1 - - [25/Jan/2025 01:14:53] \\\"GET / HTTP/1.1\\\" 404 -\\n\",\n",
    "      \"127.0.0.1 - - [25/Jan/2025 01:14:53] \\\"GET /favicon.ico HTTP/1.1\\\" 404 -\\n\",\n",
    "      \"127.0.0.1 - - [25/Jan/2025 01:16:03] \\\"GET / HTTP/1.1\\\" 404 -\\n\"\n",
    "     ]\n",
    "    }\n",
    "   ],\n",
    "   \"source\": [\n",
    "    \"from flask import Flask, request\\n\",\n",
    "    \"from twilio.twiml.messaging_response import MessagingResponse\\n\",\n",
    "    \"from googletrans import Translator\\n\",\n",
    "    \"import requests\\n\",\n",
    "    # (Remaining code continues here...)\n",
    "   ]\n",
    "  }\n",
    " ],\n",
    " \"metadata\": {\n",
    "  \"kernelspec\": {\n",
    "   \"display_name\": \"Python [conda env:base] *\",\n",
    "   \"language\": \"python\",\n",
    "   \"name\": \"conda-base-py\"\n",
    "  },\n",
    "  \"language_info\": {\n",
    "   \"codemirror_mode\": {\n",
    "    \"name\": \"ipython\",\n",
    "    \"version\": 3\n",
    "   },\n",
    "   \"file_extension\": \".py\",\n",
    "   \"mimetype\": \"text/x-python\",\n",
    "   \"name\": \"python\",\n",
    "   \"nbconvert_exporter\": \"python\",\n",
    "   \"pygments_lexer\": \"ipython3\",\n",
    "   \"version\": \"3.11.3\"\n",
    "  }\n",
    " },\n",
    " \"nbformat\": 4,\n",
    " \"nbformat_minor\": 5\n",
    "}\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
