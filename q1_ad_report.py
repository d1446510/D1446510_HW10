{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3b069d0a"
      },
      "source": [
        "# 共同設定：學號讀取與變數定義"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "a6e23da9",
        "outputId": "d7a548c1-328d-453d-f071-da7d50cf7244"
      },
      "source": [
        "# 讀取完整學號並進行格式化處理\n",
        "student_id = input(\"請輸入完整學號：\").strip().upper()\n",
        "\n",
        "# 提取末三碼及各別數字\n",
        "tail = student_id[-3:]\n",
        "a = int(student_id[-3])\n",
        "b = int(student_id[-2])\n",
        "c = int(student_id[-1])\n",
        "s = a + b + c\n",
        "\n",
        "# 驗證輸出結果\n",
        "print(f\"\\n學號 (student_id): {student_id}\")\n",
        "print(f\"末三碼 (tail): {tail}\")\n",
        "print(f\"a = {a}, b = {b}, c = {c}\")\n",
        "print(f\"s (a + b + c) = {s}\")"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "請輸入完整學號：D1446510\n",
            "\n",
            "學號 (student_id): D1446510\n",
            "末三碼 (tail): 510\n",
            "a = 5, b = 1, c = 0\n",
            "s (a + b + c) = 6\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2d24c8f3"
      },
      "source": [
        "## 第一題：製作自己的廣告成效報表"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "40a8acfb",
        "outputId": "183896fe-05d2-4051-d87c-8365a8922cb4"
      },
      "source": [
        "def ad_report(impressions, clicks, target=3.0):\n",
        "    # 曝光次數為 0 時，回傳 (None, False)\n",
        "    if impressions == 0:\n",
        "        return (None, False)\n",
        "\n",
        "    # 計算 CTR 百分比\n",
        "    ctr = (clicks / impressions) * 100\n",
        "\n",
        "    # 判斷是否達標\n",
        "    passed = ctr >= target\n",
        "    return (ctr, passed)\n",
        "\n",
        "# 產生符合學號變數的廣告數據\n",
        "ads = [\n",
        "    (\"搜尋廣告\", 1000 + 100 * a, 30 + 5 * b),\n",
        "    (\"社群廣告\", 1200 + 100 * b, 24 + 4 * c),\n",
        "    (\"影音廣告\", 0, 0),\n",
        "]\n",
        "\n",
        "# 個人 CTR 門檻\n",
        "target = 2.5 + 0.1 * c\n",
        "\n",
        "# 逐筆計算並印出報表\n",
        "print(f\"學號：{student_id}\")\n",
        "print(f\"CTR門檻：{target:.2f}%\")\n",
        "\n",
        "passed_count = 0\n",
        "for name, imp, clk in ads:\n",
        "    ctr, passed = ad_report(imp, clk, target=target)\n",
        "\n",
        "    # 格式化 CTR 顯示\n",
        "    if ctr is None:\n",
        "        ctr_display = \"無曝光資料\"\n",
        "    else:\n",
        "        ctr_display = f\"{ctr:.2f}%\"\n",
        "\n",
        "    if passed:\n",
        "        passed_count += 1\n",
        "\n",
        "    print(f\"{name}：曝光={imp}，點擊={clk}，CTR={ctr_display}，達標={passed}\")\n",
        "\n",
        "print(f\"達標廣告數：{passed_count}\")\n",
        "\n",
        "# 驗證預設門檻與零點擊測試\n",
        "default_test = ad_report(1000, 30)\n",
        "zero_click_test = ad_report(1000, 0)\n",
        "\n",
        "print(f\"預設門檻測試：{default_test}\")\n",
        "print(f\"零點擊測試：{zero_click_test}\")"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "學號：D1446510\n",
            "CTR門檻：2.50%\n",
            "搜尋廣告：曝光=1500，點擊=35，CTR=2.33%，達標=False\n",
            "社群廣告：曝光=1300，點擊=24，CTR=1.85%，達標=False\n",
            "影音廣告：曝光=0，點擊=0，CTR=無曝光資料，達標=False\n",
            "達標廣告數：0\n",
            "預設門檻測試：(3.0, True)\n",
            "零點擊測試：(0.0, False)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ff122780"
      },
      "source": [
