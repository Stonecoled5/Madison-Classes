{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# project: p9\n",
    "# submitter-netid: mwodnicki\n",
    "# partner-netid: cjohnstone\n",
    "import os, json, csv\n",
    "from operator import attrgetter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['2.json', '2.csv', '1.json', '1.csv']"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q1\n",
    "list1=os.listdir(\"sample_data\")\n",
    "list1=sorted(list1, reverse=True)\n",
    "list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['sample_data\\\\2.json',\n",
       " 'sample_data\\\\2.csv',\n",
       " 'sample_data\\\\1.json',\n",
       " 'sample_data\\\\1.csv']"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q2\n",
    "list2=[]\n",
    "for i in list1:\n",
    "    path=os.path.join(\"sample_data\", i)\n",
    "    list2.append(path)\n",
    "list2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['full_data\\\\meta.info',\n",
       " 'full_data\\\\agency_info',\n",
       " 'full_data\\\\5.json',\n",
       " 'full_data\\\\5.csv',\n",
       " 'full_data\\\\4.json',\n",
       " 'full_data\\\\4.csv',\n",
       " 'full_data\\\\3.json',\n",
       " 'full_data\\\\3.csv',\n",
       " 'full_data\\\\2.json',\n",
       " 'full_data\\\\2.csv',\n",
       " 'full_data\\\\1.json',\n",
       " 'full_data\\\\1.csv']"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q3\n",
    "list3=[]\n",
    "list1=os.listdir(\"full_data\")\n",
    "list1=sorted(list1, reverse=True)\n",
    "for i in list1:\n",
    "    path=os.path.join(\"full_data\", i)\n",
    "    list3.append(path)\n",
    "list3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['sample_data\\\\2.json',\n",
       " 'sample_data\\\\2.csv',\n",
       " 'sample_data\\\\1.json',\n",
       " 'sample_data\\\\1.csv']"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q4\n",
    "list1=[]\n",
    "for i in list2:\n",
    "    if i.find(\".json\")!=-1:\n",
    "        list1.append(i)\n",
    "    elif i.find(\".csv\")!=-1:\n",
    "        list1.append(i)\n",
    "list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['full_data\\\\5.json',\n",
       " 'full_data\\\\5.csv',\n",
       " 'full_data\\\\4.json',\n",
       " 'full_data\\\\4.csv',\n",
       " 'full_data\\\\3.json',\n",
       " 'full_data\\\\3.csv',\n",
       " 'full_data\\\\2.json',\n",
       " 'full_data\\\\2.csv',\n",
       " 'full_data\\\\1.json',\n",
       " 'full_data\\\\1.csv']"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q5\n",
    "list1=[]\n",
    "for i in list3:\n",
    "    if i.find(\".json\")!=-1:\n",
    "        list1.append(i)\n",
    "    elif i.find(\".csv\")!=-1:\n",
    "        list1.append(i)\n",
    "list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Tweet(tweet_id='1467811372', username='USERID_6', num_liked=5882, length=29),\n",
       " Tweet(tweet_id='1467811592', username='USERID_8', num_liked=2676, length=11),\n",
       " Tweet(tweet_id='1467811594', username='USERID_9', num_liked=2182, length=99),\n",
       " Tweet(tweet_id='1467811795', username='USERID_1', num_liked=7791, length=36),\n",
       " Tweet(tweet_id='1467812025', username='USERID_1', num_liked=8149, length=25)]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q6\n",
    "import collections\n",
    "def process_csv(filename):\n",
    "    exampleFile = open(filename, encoding=\"utf-8\")\n",
    "    exampleReader = csv.reader(exampleFile)\n",
    "    exampleData = list(exampleReader)\n",
    "    return exampleData\n",
    "def cell(row_idx, col_name):\n",
    "    col_idx = csv_header.index(col_name)\n",
    "    val = csv_data[row_idx][col_idx]\n",
    "    if val == \"\":\n",
    "        return None\n",
    "    return val\n",
    "Tweet = collections.namedtuple(\"Tweet\", \"tweet_id username num_liked length\")\n",
    "def csvproc(path):\n",
    "    list1=[]\n",
    "    list2=[]\n",
    "    csv_rows = process_csv(path)\n",
    "    csv_header = csv_rows[0]\n",
    "    csv_data = csv_rows[1:]\n",
    "    for i in range(len(csv_data)):\n",
    "        list2=csv_data[i]\n",
    "        if len(list2)<6:\n",
    "            continue\n",
    "        tweetid=list2[0]\n",
    "        user=list2[2]\n",
    "        numlike=list2[3]\n",
    "        leng=len(list2[4])\n",
    "        tweet=Tweet(tweet_id=str(tweetid),username=str(user),num_liked=int(numlike),length=int(leng))\n",
    "        list1.append(tweet)\n",
    "    return list1\n",
    "csvproc(\"sample_data\\\\1.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Tweet(tweet_id='1467812799', username='USERID_7', num_liked=3340, length=103),\n",
       " Tweet(tweet_id='1467812964', username='USERID_10', num_liked=3684, length=93),\n",
       " Tweet(tweet_id='1467813137', username='USERID_5', num_liked=6816, length=20),\n",
       " Tweet(tweet_id='1467813579', username='USERID_1', num_liked=1348, length=64),\n",
       " Tweet(tweet_id='1467813782', username='USERID_1', num_liked=4770, length=79)]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q7\n",
    "csvproc(\"sample_data\\\\2.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Tweet(tweet_id='1467844540', username='USERID_9', num_liked=6366, length=49),\n",
       " Tweet(tweet_id='1467844907', username='USERID_3', num_liked=8770, length=42),\n",
       " Tweet(tweet_id='1467845095', username='USERID_4', num_liked=8567, length=126),\n",
       " Tweet(tweet_id='1467845157', username='USERID_8', num_liked=5761, length=17),\n",
       " Tweet(tweet_id='1467852031', username='USERID_2', num_liked=4565, length=63),\n",
       " Tweet(tweet_id='1467852067', username='USERID_4', num_liked=9594, length=34),\n",
       " Tweet(tweet_id='1467852789', username='USERID_10', num_liked=686, length=44),\n",
       " Tweet(tweet_id='1467853135', username='USERID_1', num_liked=6515, length=131),\n",
       " Tweet(tweet_id='1467853356', username='USERID_10', num_liked=3192, length=136),\n",
       " Tweet(tweet_id='1467853431', username='USERID_10', num_liked=9936, length=30),\n",
       " Tweet(tweet_id='1467853479', username='USERID_9', num_liked=4939, length=24),\n",
       " Tweet(tweet_id='1467854062', username='USERID_10', num_liked=9346, length=92),\n",
       " Tweet(tweet_id='1467854345', username='USERID_9', num_liked=7959, length=72),\n",
       " Tweet(tweet_id='1467854706', username='USERID_1', num_liked=8972, length=103),\n",
       " Tweet(tweet_id='1467854917', username='USERID_2', num_liked=7741, length=30),\n",
       " Tweet(tweet_id='1467855673', username='USERID_9', num_liked=9728, length=72),\n",
       " Tweet(tweet_id='1467855812', username='USERID_2', num_liked=4806, length=28),\n",
       " Tweet(tweet_id='1467855981', username='USERID_2', num_liked=6455, length=92),\n",
       " Tweet(tweet_id='1467856044', username='USERID_7', num_liked=1442, length=49),\n",
       " Tweet(tweet_id='1467856352', username='USERID_3', num_liked=523, length=20),\n",
       " Tweet(tweet_id='1467856426', username='USERID_6', num_liked=8675, length=99),\n",
       " Tweet(tweet_id='1467856497', username='USERID_7', num_liked=3105, length=79),\n",
       " Tweet(tweet_id='1467856632', username='USERID_1', num_liked=1724, length=43),\n",
       " Tweet(tweet_id='1467856821', username='USERID_6', num_liked=5145, length=80),\n",
       " Tweet(tweet_id='1467856919', username='USERID_4', num_liked=3887, length=61),\n",
       " Tweet(tweet_id='1467857221', username='USERID_5', num_liked=3589, length=102),\n",
       " Tweet(tweet_id='1467857297', username='USERID_1', num_liked=736, length=70),\n",
       " Tweet(tweet_id='1467857378', username='USERID_4', num_liked=9459, length=81),\n",
       " Tweet(tweet_id='1467857511', username='USERID_7', num_liked=3713, length=127),\n",
       " Tweet(tweet_id='1467857722', username='USERID_8', num_liked=9072, length=55),\n",
       " Tweet(tweet_id='1467857975', username='USERID_9', num_liked=4893, length=21),\n",
       " Tweet(tweet_id='1467858363', username='USERID_10', num_liked=4263, length=119),\n",
       " Tweet(tweet_id='1467858627', username='USERID_3', num_liked=8400, length=120),\n",
       " Tweet(tweet_id='1467858869', username='USERID_10', num_liked=1609, length=48),\n",
       " Tweet(tweet_id='1467859025', username='USERID_4', num_liked=5618, length=81),\n",
       " Tweet(tweet_id='1467859066', username='USERID_9', num_liked=99, length=53),\n",
       " Tweet(tweet_id='1467859408', username='USERID_5', num_liked=2878, length=128),\n",
       " Tweet(tweet_id='1467859436', username='USERID_7', num_liked=8001, length=67),\n",
       " Tweet(tweet_id='1467859558', username='USERID_1', num_liked=8732, length=136),\n",
       " Tweet(tweet_id='1467859666', username='USERID_9', num_liked=9158, length=16),\n",
       " Tweet(tweet_id='1467859820', username='USERID_10', num_liked=7921, length=27),\n",
       " Tweet(tweet_id='1467859922', username='USERID_6', num_liked=3955, length=120),\n",
       " Tweet(tweet_id='1467860895', username='USERID_1', num_liked=2055, length=18),\n",
       " Tweet(tweet_id='1467860904', username='USERID_7', num_liked=9851, length=30),\n",
       " Tweet(tweet_id='1467861095', username='USERID_10', num_liked=7191, length=38),\n",
       " Tweet(tweet_id='1467861522', username='USERID_1', num_liked=2742, length=70),\n",
       " Tweet(tweet_id='1467861571', username='USERID_1', num_liked=7095, length=84),\n",
       " Tweet(tweet_id='1467862213', username='USERID_2', num_liked=2455, length=138),\n",
       " Tweet(tweet_id='1467862313', username='USERID_10', num_liked=3256, length=127),\n",
       " Tweet(tweet_id='1467862355', username='USERID_3', num_liked=4110, length=53)]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q8\n",
    "csvproc(\"full_data\\\\1.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Tweet(tweet_id='1467876711', username='USERID_10', num_liked=1117, length=84),\n",
       " Tweet(tweet_id='1467877496', username='USERID_1', num_liked=2062, length=106),\n",
       " Tweet(tweet_id='1467877833', username='USERID_2', num_liked=4270, length=89),\n",
       " Tweet(tweet_id='1467877865', username='USERID_1', num_liked=5899, length=30),\n",
       " Tweet(tweet_id='1467878057', username='USERID_6', num_liked=703, length=42),\n",
       " Tweet(tweet_id='1467878557', username='USERID_6', num_liked=5814, length=61),\n",
       " Tweet(tweet_id='1467878633', username='USERID_2', num_liked=2351, length=33),\n",
       " Tweet(tweet_id='1467878971', username='USERID_2', num_liked=2238, length=27),\n",
       " Tweet(tweet_id='1467878983', username='USERID_8', num_liked=4860, length=61),\n",
       " Tweet(tweet_id='1467879480', username='USERID_4', num_liked=1345, length=97),\n",
       " Tweet(tweet_id='1467879984', username='USERID_2', num_liked=3694, length=69),\n",
       " Tweet(tweet_id='1467880085', username='USERID_4', num_liked=2478, length=120),\n",
       " Tweet(tweet_id='1467880431', username='USERID_3', num_liked=9407, length=85),\n",
       " Tweet(tweet_id='1467880442', username='USERID_2', num_liked=5125, length=96),\n",
       " Tweet(tweet_id='1467880463', username='USERID_9', num_liked=1226, length=29),\n",
       " Tweet(tweet_id='1467880692', username='USERID_6', num_liked=4989, length=49),\n",
       " Tweet(tweet_id='1467881131', username='USERID_10', num_liked=732, length=107),\n",
       " Tweet(tweet_id='1467881373', username='USERID_6', num_liked=8615, length=145),\n",
       " Tweet(tweet_id='1467881376', username='USERID_4', num_liked=4378, length=49),\n",
       " Tweet(tweet_id='1467881457', username='USERID_7', num_liked=119, length=27),\n",
       " Tweet(tweet_id='1467881686', username='USERID_5', num_liked=8136, length=46),\n",
       " Tweet(tweet_id='1467881809', username='USERID_4', num_liked=1797, length=138),\n",
       " Tweet(tweet_id='1467881897', username='USERID_5', num_liked=2314, length=76),\n",
       " Tweet(tweet_id='1467881920', username='USERID_3', num_liked=4101, length=112),\n",
       " Tweet(tweet_id='1467882140', username='USERID_8', num_liked=5320, length=137),\n",
       " Tweet(tweet_id='1467882491', username='USERID_10', num_liked=3512, length=55),\n",
       " Tweet(tweet_id='1467882592', username='USERID_10', num_liked=1887, length=67),\n",
       " Tweet(tweet_id='1467882902', username='USERID_3', num_liked=4646, length=48),\n",
       " Tweet(tweet_id='1467888679', username='USERID_8', num_liked=3089, length=27),\n",
       " Tweet(tweet_id='1467888732', username='USERID_7', num_liked=2800, length=48),\n",
       " Tweet(tweet_id='1467888953', username='USERID_3', num_liked=3951, length=46),\n",
       " Tweet(tweet_id='1467889231', username='USERID_5', num_liked=1320, length=79),\n",
       " Tweet(tweet_id='1467889334', username='USERID_5', num_liked=8495, length=42),\n",
       " Tweet(tweet_id='1467889574', username='USERID_1', num_liked=4696, length=123),\n",
       " Tweet(tweet_id='1467889791', username='USERID_5', num_liked=4027, length=132),\n",
       " Tweet(tweet_id='1467889988', username='USERID_2', num_liked=7394, length=51),\n",
       " Tweet(tweet_id='1467890079', username='USERID_8', num_liked=2556, length=38),\n",
       " Tweet(tweet_id='1467890222', username='USERID_2', num_liked=227, length=107),\n",
       " Tweet(tweet_id='1467890723', username='USERID_1', num_liked=96, length=134),\n",
       " Tweet(tweet_id='1467891826', username='USERID_9', num_liked=2021, length=113),\n",
       " Tweet(tweet_id='1467891880', username='USERID_7', num_liked=6847, length=96),\n",
       " Tweet(tweet_id='1467892075', username='USERID_6', num_liked=2816, length=124),\n",
       " Tweet(tweet_id='1467892515', username='USERID_5', num_liked=917, length=39),\n",
       " Tweet(tweet_id='1467892667', username='USERID_2', num_liked=8270, length=20),\n",
       " Tweet(tweet_id='1467892720', username='USERID_3', num_liked=3227, length=128)]"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q9\n",
    "csvproc(\"full_data\\\\2.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Tweet(tweet_id='1467810369', username='USERID_4', num_liked=315, length=115),\n",
       " Tweet(tweet_id='1467810672', username='USERID_8', num_liked=5298, length=111),\n",
       " Tweet(tweet_id='1467810917', username='USERID_8', num_liked=533, length=89),\n",
       " Tweet(tweet_id='1467811184', username='USERID_6', num_liked=2650, length=47),\n",
       " Tweet(tweet_id='1467811193', username='USERID_8', num_liked=2101, length=111)]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q10\n",
    "def json1(dire, file):\n",
    "    list1=[]\n",
    "    f = open(os.path.join(dire, file), encoding=\"utf-8\")\n",
    "    try:\n",
    "        data = json.load(f)\n",
    "    except ValueError:\n",
    "        data=[]\n",
    "        return data\n",
    "    f.close()\n",
    "    for i in data:\n",
    "        tweetid=i\n",
    "        user=data[i][\"username\"]\n",
    "        numlike=data[i][\"num_liked\"]\n",
    "        if type(numlike) is str:\n",
    "            if numlike.endswith(\"M\"):\n",
    "                numlike=numlike[:3]\n",
    "                numlike=int(numlike)*1000000\n",
    "            elif numlike.endswith(\"k\"):\n",
    "                numlike=numlike[:3]\n",
    "                numlike=int(numlike)*1000\n",
    "            else:\n",
    "                continue\n",
    "        leng=len(data[i][\"tweet_text\"])\n",
    "        tweet=Tweet(tweet_id=tweetid,username=user,num_liked=numlike,length=leng)\n",
    "        list1.append(tweet)\n",
    "    return list1\n",
    "json1(\"sample_data\", \"1.json\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Tweet(tweet_id='1467812416', username='USERID_9', num_liked=5278, length=43),\n",
       " Tweet(tweet_id='1467812579', username='USERID_1', num_liked=9700, length=26),\n",
       " Tweet(tweet_id='1467812723', username='USERID_3', num_liked=5414, length=94),\n",
       " Tweet(tweet_id='1467812771', username='USERID_8', num_liked=2190, length=77),\n",
       " Tweet(tweet_id='1467812784', username='USERID_10', num_liked=2667, length=117)]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q11\n",
    "json1(\"sample_data\", \"2.json\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Tweet(tweet_id='1467944581', username='USERID_1', num_liked=7216, length=131),\n",
       " Tweet(tweet_id='1467944654', username='USERID_7', num_liked=2838, length=59),\n",
       " Tweet(tweet_id='1467944871', username='USERID_1', num_liked=9393, length=51),\n",
       " Tweet(tweet_id='1467945476', username='USERID_10', num_liked=9246, length=33),\n",
       " Tweet(tweet_id='1467945704', username='USERID_1', num_liked=526, length=62),\n",
       " Tweet(tweet_id='1467945787', username='USERID_9', num_liked=8850, length=81),\n",
       " Tweet(tweet_id='1467945885', username='USERID_4', num_liked=9403, length=67),\n",
       " Tweet(tweet_id='1467946026', username='USERID_1', num_liked=2861, length=69),\n",
       " Tweet(tweet_id='1467946137', username='USERID_1', num_liked=5470, length=135),\n",
       " Tweet(tweet_id='1467946559', username='USERID_6', num_liked=987, length=116),\n",
       " Tweet(tweet_id='1467946592', username='USERID_3', num_liked=9085, length=137),\n",
       " Tweet(tweet_id='1467946749', username='USERID_4', num_liked=3381, length=42),\n",
       " Tweet(tweet_id='1467946810', username='USERID_4', num_liked=5338, length=62),\n",
       " Tweet(tweet_id='1467947005', username='USERID_7', num_liked=6974, length=53),\n",
       " Tweet(tweet_id='1467947104', username='USERID_6', num_liked=5847, length=24),\n",
       " Tweet(tweet_id='1467947557', username='USERID_9', num_liked=8449, length=110),\n",
       " Tweet(tweet_id='1467947713', username='USERID_7', num_liked=7444, length=140),\n",
       " Tweet(tweet_id='1467947913', username='USERID_2', num_liked=8578, length=36),\n",
       " Tweet(tweet_id='1467948169', username='USERID_1', num_liked=4545, length=33),\n",
       " Tweet(tweet_id='1467948434', username='USERID_9', num_liked=770, length=53),\n",
       " Tweet(tweet_id='1467948521', username='USERID_4', num_liked=8276, length=100),\n",
       " Tweet(tweet_id='1467948526', username='USERID_3', num_liked=7010, length=64),\n",
       " Tweet(tweet_id='1467948979', username='USERID_10', num_liked=9209, length=93),\n",
       " Tweet(tweet_id='1467949047', username='USERID_3', num_liked=7231, length=30),\n",
       " Tweet(tweet_id='1467949516', username='USERID_3', num_liked=4787, length=104),\n",
       " Tweet(tweet_id='1467949681', username='USERID_5', num_liked=5318, length=36),\n",
       " Tweet(tweet_id='1467949746', username='USERID_8', num_liked=4383, length=8),\n",
       " Tweet(tweet_id='1467949969', username='USERID_3', num_liked=1177, length=80),\n",
       " Tweet(tweet_id='1467950027', username='USERID_10', num_liked=8575, length=26),\n",
       " Tweet(tweet_id='1467950029', username='USERID_1', num_liked=7362, length=119),\n",
       " Tweet(tweet_id='1467950217', username='USERID_7', num_liked=1241, length=63),\n",
       " Tweet(tweet_id='1467950510', username='USERID_7', num_liked=5002, length=34),\n",
       " Tweet(tweet_id='1467950588', username='USERID_4', num_liked=589, length=63),\n",
       " Tweet(tweet_id='1467950600', username='USERID_3', num_liked=5951, length=71),\n",
       " Tweet(tweet_id='1467950649', username='USERID_7', num_liked=9449, length=46),\n",
       " Tweet(tweet_id='1467950687', username='USERID_3', num_liked=3464, length=70),\n",
       " Tweet(tweet_id='1467950866', username='USERID_4', num_liked=122, length=27),\n",
       " Tweet(tweet_id='1467950975', username='USERID_3', num_liked=6793, length=74),\n",
       " Tweet(tweet_id='1467951016', username='USERID_5', num_liked=7795, length=80),\n",
       " Tweet(tweet_id='1467951035', username='USERID_9', num_liked=3477, length=114),\n",
       " Tweet(tweet_id='1467951252', username='USERID_2', num_liked=7515, length=48),\n",
       " Tweet(tweet_id='1467951422', username='USERID_6', num_liked=2520, length=98),\n",
       " Tweet(tweet_id='1467951568', username='USERID_8', num_liked=39, length=98),\n",
       " Tweet(tweet_id='1467951850', username='USERID_8', num_liked=1170, length=29),\n",
       " Tweet(tweet_id='1467951931', username='USERID_4', num_liked=5320, length=81),\n",
       " Tweet(tweet_id='1467952069', username='USERID_7', num_liked=399, length=24),\n",
       " Tweet(tweet_id='1467952100', username='USERID_1', num_liked=2754, length=69),\n",
       " Tweet(tweet_id='1467952123', username='USERID_9', num_liked=9222, length=137),\n",
       " Tweet(tweet_id='1467952985', username='USERID_4', num_liked=6256, length=118),\n",
       " Tweet(tweet_id='1467953090', username='USERID_2', num_liked=1896, length=64)]"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q12\n",
    "json1(\"full_data\", \"5.json\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q13\n",
    "json1(\"full_data\", \"1.json\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'sample_data\\\\2.csv'"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q14\n",
    "def paths(dire, num):\n",
    "    yes=False\n",
    "    list1=[]\n",
    "    for filename in os.listdir(dire):\n",
    "        if filename.endswith(\".json\"):\n",
    "            dic=json1(dire, filename)\n",
    "            for i in dic:\n",
    "                if i.tweet_id==num:\n",
    "                    yes=True\n",
    "                    dicy=os.path.join(dire, filename)\n",
    "                    break\n",
    "        else:\n",
    "            dic=csvproc(dire+\"\\\\\"+filename)\n",
    "            for i in dic:\n",
    "                if i.tweet_id==num:\n",
    "                    yes=True\n",
    "                    dicy=os.path.join(dire, filename)\n",
    "                    break\n",
    "    if yes==True:\n",
    "        yes=dicy\n",
    "    return yes\n",
    "paths(\"sample_data\", \"1467813137\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q15\n",
    "paths(\"full_data\", \"1467862937\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'full_data\\\\3.csv'"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q16\n",
    "paths(\"full_data\", \"1467907751\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['sample_data\\\\2.json', 'sample_data\\\\2.csv', 'sample_data\\\\1.csv']"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q17\n",
    "yes=False\n",
    "list1=[]\n",
    "for filename in os.listdir(\"sample_data\"):\n",
    "    if filename.endswith(\".json\"):\n",
    "        dic=json1(\"sample_data\", filename)\n",
    "        for i in dic:\n",
    "            if i.username==\"USERID_1\":\n",
    "                yes=True\n",
    "                dicy=os.path.join(\"sample_data\", filename)\n",
    "                list1.append(dicy)\n",
    "                break\n",
    "    else:\n",
    "        dic=csvproc(\"sample_data\\\\\"+filename)\n",
    "        for i in dic:\n",
    "            if i.username==\"USERID_1\":\n",
    "                yes=True\n",
    "                dicy=os.path.join(\"sample_data\", filename)\n",
    "                list1.append(dicy)\n",
    "                break\n",
    "if yes==True:\n",
    "    yes=sorted(list1, reverse=True)\n",
    "yes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Tweet(tweet_id='1467810369', username='USERID_4', num_liked=315, length=115),\n",
       " Tweet(tweet_id='1467810672', username='USERID_8', num_liked=5298, length=111),\n",
       " Tweet(tweet_id='1467810917', username='USERID_8', num_liked=533, length=89),\n",
       " Tweet(tweet_id='1467811184', username='USERID_6', num_liked=2650, length=47),\n",
       " Tweet(tweet_id='1467811193', username='USERID_8', num_liked=2101, length=111),\n",
       " Tweet(tweet_id='1467811372', username='USERID_6', num_liked=5882, length=29),\n",
       " Tweet(tweet_id='1467811592', username='USERID_8', num_liked=2676, length=11),\n",
       " Tweet(tweet_id='1467811594', username='USERID_9', num_liked=2182, length=99),\n",
       " Tweet(tweet_id='1467811795', username='USERID_1', num_liked=7791, length=36),\n",
       " Tweet(tweet_id='1467812025', username='USERID_1', num_liked=8149, length=25),\n",
       " Tweet(tweet_id='1467812416', username='USERID_9', num_liked=5278, length=43),\n",
       " Tweet(tweet_id='1467812579', username='USERID_1', num_liked=9700, length=26),\n",
       " Tweet(tweet_id='1467812723', username='USERID_3', num_liked=5414, length=94),\n",
       " Tweet(tweet_id='1467812771', username='USERID_8', num_liked=2190, length=77),\n",
       " Tweet(tweet_id='1467812784', username='USERID_10', num_liked=2667, length=117),\n",
       " Tweet(tweet_id='1467812799', username='USERID_7', num_liked=3340, length=103),\n",
       " Tweet(tweet_id='1467812964', username='USERID_10', num_liked=3684, length=93),\n",
       " Tweet(tweet_id='1467813137', username='USERID_5', num_liked=6816, length=20),\n",
       " Tweet(tweet_id='1467813579', username='USERID_1', num_liked=1348, length=64),\n",
       " Tweet(tweet_id='1467813782', username='USERID_1', num_liked=4770, length=79)]"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q18\n",
    "list1=[]\n",
    "for filename in os.listdir(\"sample_data\"):\n",
    "    if filename.endswith(\".json\"):\n",
    "        dic=json1(\"sample_data\", filename)\n",
    "        for i in dic:\n",
    "            list1.append(i)\n",
    "    else:\n",
    "        dic=csvproc(\"sample_data\\\\\"+filename)\n",
    "        for i in dic:\n",
    "            list1.append(i)\n",
    "list1=sorted(list1, key=attrgetter('tweet_id'))\n",
    "list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Tweet(tweet_id='1467812579', username='USERID_1', num_liked=9700, length=26),\n",
       " Tweet(tweet_id='1467812025', username='USERID_1', num_liked=8149, length=25),\n",
       " Tweet(tweet_id='1467811795', username='USERID_1', num_liked=7791, length=36),\n",
       " Tweet(tweet_id='1467813137', username='USERID_5', num_liked=6816, length=20),\n",
       " Tweet(tweet_id='1467811372', username='USERID_6', num_liked=5882, length=29),\n",
       " Tweet(tweet_id='1467812723', username='USERID_3', num_liked=5414, length=94),\n",
       " Tweet(tweet_id='1467810672', username='USERID_8', num_liked=5298, length=111),\n",
       " Tweet(tweet_id='1467812416', username='USERID_9', num_liked=5278, length=43),\n",
       " Tweet(tweet_id='1467813782', username='USERID_1', num_liked=4770, length=79),\n",
       " Tweet(tweet_id='1467812964', username='USERID_10', num_liked=3684, length=93),\n",
       " Tweet(tweet_id='1467812799', username='USERID_7', num_liked=3340, length=103),\n",
       " Tweet(tweet_id='1467811592', username='USERID_8', num_liked=2676, length=11),\n",
       " Tweet(tweet_id='1467812784', username='USERID_10', num_liked=2667, length=117),\n",
       " Tweet(tweet_id='1467811184', username='USERID_6', num_liked=2650, length=47),\n",
       " Tweet(tweet_id='1467812771', username='USERID_8', num_liked=2190, length=77),\n",
       " Tweet(tweet_id='1467811594', username='USERID_9', num_liked=2182, length=99),\n",
       " Tweet(tweet_id='1467811193', username='USERID_8', num_liked=2101, length=111),\n",
       " Tweet(tweet_id='1467813579', username='USERID_1', num_liked=1348, length=64),\n",
       " Tweet(tweet_id='1467810917', username='USERID_8', num_liked=533, length=89),\n",
       " Tweet(tweet_id='1467810369', username='USERID_4', num_liked=315, length=115)]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q19\n",
    "list1=sorted(list1, key=attrgetter('num_liked'), reverse=True)\n",
    "list1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[Tweet(tweet_id='1467894593', username='USERID_2', num_liked=869000000, length=136),\n",
       " Tweet(tweet_id='1467894600', username='USERID_8', num_liked=915000, length=67),\n",
       " Tweet(tweet_id='1467853431', username='USERID_10', num_liked=9936, length=30),\n",
       " Tweet(tweet_id='1467875163', username='USERID_2', num_liked=9891, length=69),\n",
       " Tweet(tweet_id='1467860904', username='USERID_7', num_liked=9851, length=30),\n",
       " Tweet(tweet_id='1467928014', username='USERID_7', num_liked=9830, length=18),\n",
       " Tweet(tweet_id='1467895048', username='USERID_10', num_liked=9822, length=136),\n",
       " Tweet(tweet_id='1467966646', username='USERID_7', num_liked=9821, length=47),\n",
       " Tweet(tweet_id='1467855673', username='USERID_9', num_liked=9728, length=72),\n",
       " Tweet(tweet_id='1467898078', username='USERID_10', num_liked=9705, length=104),\n",
       " Tweet(tweet_id='1467928300', username='USERID_9', num_liked=9681, length=79),\n",
       " Tweet(tweet_id='1467917177', username='USERID_3', num_liked=9678, length=105),\n",
       " Tweet(tweet_id='1467923235', username='USERID_9', num_liked=9662, length=134),\n",
       " Tweet(tweet_id='1467964211', username='USERID_4', num_liked=9618, length=79),\n",
       " Tweet(tweet_id='1467873980', username='USERID_5', num_liked=9608, length=88),\n",
       " Tweet(tweet_id='1467852067', username='USERID_4', num_liked=9594, length=34),\n",
       " Tweet(tweet_id='1467863633', username='USERID_9', num_liked=9549, length=95),\n",
       " Tweet(tweet_id='1467953733', username='USERID_4', num_liked=9526, length=67),\n",
       " Tweet(tweet_id='1467862806', username='USERID_2', num_liked=9465, length=68),\n",
       " Tweet(tweet_id='1467954070', username='USERID_8', num_liked=9462, length=64)]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#q20\n",
    "list1=[]\n",
    "for filename in os.listdir(\"full_data\"):\n",
    "    if filename.endswith(\".json\"):\n",
    "        dic=json1(\"full_data\", filename)\n",
    "        for i in dic:\n",
    "            list1.append(i)\n",
    "    else:\n",
    "        dic=csvproc(\"full_data\\\\\"+filename)\n",
    "        for i in dic:\n",
    "            list1.append(i)\n",
    "list1=sorted(list1, key=attrgetter('num_liked'), reverse=True)\n",
    "list1[:20]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
