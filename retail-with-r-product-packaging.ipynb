{
 "cells": [
  {
   "cell_type": "markdown",
   "execution_count": null,
   "metadata": {
    "_cell_guid": "52c66cff-9882-4055-94e0-40128bd3d8d9",
    "_uuid": "6d5658ad-32fd-48c3-b63c-070fb691f21a"
   },
   "source": [
    "# **Statistik Top 10 Transaksi Produk**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "_cell_guid": "1d351cbb-b6ce-43f4-874d-de3c55e6532c",
    "_execution_state": "idle",
    "_uuid": "b33a51dc-f4c7-4a18-82f7-7c6096b59ceb"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Loading required package: Matrix\n",
      "\n",
      "\n",
      "Attaching package: ‘arules’\n",
      "\n",
      "\n",
      "The following objects are masked from ‘package:base’:\n",
      "\n",
      "    abbreviate, write\n",
      "\n",
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                 Nama.Produk Jumlah\n",
      "1               Shampo Biasa   2075\n",
      "2              Serum Vitamin   1685\n",
      "3          Baju Batik Wanita   1312\n",
      "4          Baju Kemeja Putih   1255\n",
      "5       Celana Jogger Casual   1136\n",
      "6                Cover Koper   1086\n",
      "7         Sepatu Sandal Anak   1062\n",
      "8  Tali Pinggang Gesper Pria   1003\n",
      "9        Sepatu Sport merk Z    888\n",
      "10              Wedges Hitam    849\n"
     ]
    }
   ],
   "source": [
    "library(arules)\n",
    "transaksi <- read.transactions(file=\"../input/transaksi_retail.tsv\", format=\"single\", sep=\"\\t\", cols=c(1,2), skip=1)\n",
    "\n",
    "data_transaksi <- itemFrequency(transaksi, type=\"absolute\")\n",
    "data_transaksi <- sort(data_transaksi, decreasing=TRUE)\n",
    "data_transaksi <- data_transaksi[1:10]\n",
    "\n",
    "df_data <- data.frame(\"Nama Produk\"=names(data_transaksi), \"Jumlah\"=data_transaksi, row.names=NULL)\n",
    "\n",
    "print(df_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "execution_count": null,
   "metadata": {
    "_cell_guid": "4eb6e60f-6373-4f64-9b2d-a6912d468a14",
    "_uuid": "03ef2445-a17b-4784-b427-fd7ec2321202"
   },
   "source": [
    "# **Statistik Bottom 10 Transaksi Produk**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "_cell_guid": "cd0d9c79-85ca-4f1e-b167-12adc21e4694",
    "_uuid": "3aa4ef51-97b7-43c4-87ad-bce81b0f5fb5"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                  Nama.Produk Jumlah\n",
      "1     Celana Jeans Sobek Pria      9\n",
      "2                Tas Kosmetik     11\n",
      "3                Stripe Pants     19\n",
      "4                    Pelembab     24\n",
      "5      Tali Ban Ikat Pinggang     27\n",
      "6  Baju Renang Pria Anak-anak     32\n",
      "7                    Hair Dye     46\n",
      "8          Atasan Baju Belang     56\n",
      "9  Tas Sekolah Anak Perempuan     71\n",
      "10              Dompet Unisex     75\n"
     ]
    }
   ],
   "source": [
    "data_item <- itemFrequency(transaksi, type=\"absolute\")\n",
    "data_item <- sort(data_item, decreasing=FALSE)\n",
    "data_item <- data_item[1:10]\n",
    "\n",
    "df_transaksi <- data.frame(\"Nama Produk\"=names(data_item), \"Jumlah\"=data_item, row.names=NULL)\n",
    "print(df_transaksi)"
   ]
  },
  {
   "cell_type": "markdown",
   "execution_count": null,
   "metadata": {
    "_cell_guid": "442b5c51-f26e-495f-a95c-639775ccefb4",
    "_uuid": "edaf80c3-5a8b-40f5-acd5-b52e4657c596"
   },
   "source": [
    "# **Mencari Kombinasi Produk yang menarik**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "_cell_guid": "9a26a851-63b8-4592-9a85-78b908a14430",
    "_uuid": "ac84c4f3-564a-4f4b-ae1f-c1078cbe8463"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Apriori\n",
      "\n",
      "Parameter specification:\n",
      " confidence minval smax arem  aval originalSupport maxtime     support minlen\n",
      "        0.5    0.1    1 none FALSE            TRUE       5 0.002898551      2\n",
      " maxlen target  ext\n",
      "      3  rules TRUE\n",
      "\n",
      "Algorithmic control:\n",
      " filter tree heap memopt load sort verbose\n",
      "    0.1 TRUE TRUE  FALSE TRUE    2    TRUE\n",
      "\n",
      "Absolute minimum support count: 10 \n",
      "\n",
      "set item appearances ...[0 item(s)] done [0.00s].\n",
      "set transactions ...[69 item(s), 3450 transaction(s)] done [0.00s].\n",
      "sorting and recoding items ... [68 item(s)] done [0.00s].\n",
      "creating transaction tree ... done [0.00s].\n",
      "checking subsets of size 1 2 3"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Warning message in apriori(transaksi, parameter = list(supp = 10/length(transaksi), :\n",
      "“Mining stopped (maxlen reached). Only patterns up to a length of 3 returned!”\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " done [0.01s].\n",
      "writing ... [4637 rule(s)] done [0.00s].\n",
      "creating S4 object  ... done [0.00s].\n",
      "     lhs                             rhs                              support confidence    coverage     lift count\n",
      "[1]  {Tas Makeup,                                                                                                  \n",
      "      Tas Pinggang Wanita}        => {Baju Renang Anak Perempuan} 0.010434783  0.8780488 0.011884058 24.42958    36\n",
      "[2]  {Tas Makeup,                                                                                                  \n",
      "      Tas Travel}                 => {Baju Renang Anak Perempuan} 0.010144928  0.8139535 0.012463768 22.64629    35\n",
      "[3]  {Tas Makeup,                                                                                                  \n",
      "      Tas Ransel Mini}            => {Baju Renang Anak Perempuan} 0.011304348  0.7358491 0.015362319 20.47322    39\n",
      "[4]  {Sunblock Cream,                                                                                              \n",
      "      Tas Pinggang Wanita}        => {Kuas Makeup }               0.016231884  0.6913580 0.023478261 20.21343    56\n",
      "[5]  {Baju Renang Anak Perempuan,                                                                                  \n",
      "      Tas Pinggang Wanita}        => {Tas Makeup}                 0.010434783  0.8000000 0.013043478 19.57447    36\n",
      "[6]  {Baju Renang Anak Perempuan,                                                                                  \n",
      "      Tas Ransel Mini}            => {Tas Makeup}                 0.011304348  0.7959184 0.014202899 19.47460    39\n",
      "[7]  {Baju Renang Anak Perempuan,                                                                                  \n",
      "      Celana Pendek Green/Hijau}  => {Tas Makeup}                 0.010144928  0.7777778 0.013043478 19.03073    35\n",
      "[8]  {Tas Makeup,                                                                                                  \n",
      "      Tas Waist Bag}              => {Baju Renang Anak Perempuan} 0.004347826  0.6818182 0.006376812 18.96994    15\n",
      "[9]  {Celana Pendek Green/Hijau,                                                                                   \n",
      "      Tas Makeup}                 => {Baju Renang Anak Perempuan} 0.010144928  0.6730769 0.015072464 18.72674    35\n",
      "[10] {Dompet Flip Cover,                                                                                           \n",
      "      Sunblock Cream}             => {Kuas Makeup }               0.016231884  0.6292135 0.025797101 18.39650    56\n"
     ]
    }
   ],
   "source": [
    "mba <-apriori(transaksi, parameter = list(supp = 10/length(transaksi), minlen=2, maxlen=3,confidence = 0.5))\n",
    "\n",
    "data_transaksi <- sort(mba,by='lift', decreasing=TRUE)\n",
    "data_transaksi <- head(data_transaksi,10)\n",
    "inspect(data_transaksi)"
   ]
  },
  {
   "cell_type": "markdown",
   "execution_count": null,
   "metadata": {
    "_cell_guid": "eef13769-3041-4dd4-8d83-f3257c4fc2cf",
    "_uuid": "388bf11f-f1f3-4bf8-be2a-eaaa2f397bea"
   },
   "source": [
    "# **Mencari Paket Produk yang bisa dipasangkan dengan Item Slow-Moving(Untuk Produk \"Tas Makeup\" dan \"Baju Renang Pria Anak-anak\")**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "_cell_guid": "4be44164-463e-400a-8e9d-8e6b8b3dc739",
    "_uuid": "cd8c2b83-3f42-4808-a9c0-3375c7bdf920"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Apriori\n",
      "\n",
      "Parameter specification:\n",
      " confidence minval smax arem  aval originalSupport maxtime     support minlen\n",
      "        0.1    0.1    1 none FALSE            TRUE       5 0.002898551      2\n",
      " maxlen target  ext\n",
      "      3  rules TRUE\n",
      "\n",
      "Algorithmic control:\n",
      " filter tree heap memopt load sort verbose\n",
      "    0.1 TRUE TRUE  FALSE TRUE    2    TRUE\n",
      "\n",
      "Absolute minimum support count: 10 \n",
      "\n",
      "set item appearances ...[0 item(s)] done [0.00s].\n",
      "set transactions ...[69 item(s), 3450 transaction(s)] done [0.00s].\n",
      "sorting and recoding items ... [68 item(s)] done [0.00s].\n",
      "creating transaction tree ... done [0.00s].\n",
      "checking subsets of size 1 2 3"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Warning message in apriori(transaksi, parameter = list(supp = 10/length(transaksi), :\n",
      "“Mining stopped (maxlen reached). Only patterns up to a length of 3 returned!”\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " done [0.01s].\n",
      "writing ... [39832 rule(s)] done [0.01s].\n",
      "creating S4 object  ... done [0.01s].\n",
      "    lhs                             rhs                              support confidence   coverage     lift count\n",
      "[1] {Baju Renang Anak Perempuan,                                                                                 \n",
      "     Tas Pinggang Wanita}        => {Tas Makeup}                 0.010434783  0.8000000 0.01304348 19.57447    36\n",
      "[2] {Baju Renang Anak Perempuan,                                                                                 \n",
      "     Tas Ransel Mini}            => {Tas Makeup}                 0.011304348  0.7959184 0.01420290 19.47460    39\n",
      "[3] {Baju Renang Anak Perempuan,                                                                                 \n",
      "     Celana Pendek Green/Hijau}  => {Tas Makeup}                 0.010144928  0.7777778 0.01304348 19.03073    35\n",
      "[4] {Gembok Koper,                                                                                               \n",
      "     Tas Waist Bag}              => {Baju Renang Pria Anak-anak} 0.004057971  0.2745098 0.01478261 29.59559    14\n",
      "[5] {Flat Shoes Ballerina,                                                                                       \n",
      "     Gembok Koper}               => {Baju Renang Pria Anak-anak} 0.004057971  0.1866667 0.02173913 20.12500    14\n",
      "[6] {Celana Jeans Sobek Wanita,                                                                                  \n",
      "     Jeans Jumbo}                => {Baju Renang Pria Anak-anak} 0.005507246  0.1210191 0.04550725 13.04737    19\n"
     ]
    }
   ],
   "source": [
    "mba <- apriori(transaksi,parameter = list(supp = 10/length(transaksi),minlen=2, maxlen=3, confidence = 0.1))\n",
    "\n",
    "subset1 <- subset(mba,rhs %in% \"Tas Makeup\")\n",
    "subset2 <- subset(mba,rhs %in% \"Baju Renang Pria Anak-anak\")\n",
    "\n",
    "data_transaksi1 <- sort(subset1,by='lift', decreasing=TRUE)\n",
    "data_transaksi2 <- sort(subset2,by='lift', decreasing=TRUE)\n",
    "\n",
    "data_transaksi1 <- head(data_transaksi1,3)\n",
    "data_transaksi2 <- head(data_transaksi2,3)\n",
    "\n",
    "total_data <- c(data_transaksi1, data_transaksi2)\n",
    "inspect(total_data)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "R",
   "language": "R",
   "name": "ir"
  },
  "language_info": {
   "codemirror_mode": "r",
   "file_extension": ".r",
   "mimetype": "text/x-r-source",
   "name": "R",
   "pygments_lexer": "r",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
