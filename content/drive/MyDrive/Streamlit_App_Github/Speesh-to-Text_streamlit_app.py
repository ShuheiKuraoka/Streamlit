{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Colab_ArgoTunnel_Speech-to-Text-Streamlit",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ShuheiKuraoka/Streamlit/blob/main/content/drive/MyDrive/Streamlit_App_Github/Speesh-to-Text_streamlit_app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vWmc_s2ezvU0"
      },
      "source": [
        "#Argo TunnelでStreamlit文字起こしアプリをColabから外部公開する"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4CVM5Cvl8CJf",
        "outputId": "1f1f074c-a716-474d-a68e-020524a2bf99"
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Mounted at /content/drive\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MJHe4vtUf-Pg"
      },
      "source": [
        "#文字起こしアプリを動かす場合\n",
        "!pip install --upgrade google-cloud-speech"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RvlYkCQ9vFiy"
      },
      "source": [
        "!pip install -q streamlit   \n",
        "# エラーが出たら2回目を実行する\n",
        "# -q, --quiet : Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, and CRITICAL logging levels)."
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Xjv_W6tN56l8"
      },
      "source": [
        "!streamlit --version"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VSPUMEHYwqng"
      },
      "source": [
        "# streamlit appを バックグラウンド起動。　ログを書き出して後で起動確認できるようにもします。\n",
        "%%bash --bg\n",
        "streamlit run  /content/drive/MyDrive/Speesh-to-Text_streamlit_app.py > debug.log 2>&1"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "background_save": true
        },
        "id": "6679q_6fwsJH"
      },
      "source": [
        "# cloudflaredのインストール　＆　localhostの8501ポートのトンネリングしたアクセス用URLを発行\n",
        "!wget https://bin.equinox.io/c/VdrWdbjqyF/cloudflared-stable-linux-amd64.deb\n",
        "!dpkg -i cloudflared-stable-linux-amd64.deb\n",
        "!cloudflared tunnel --url localhost:8501"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IqxMcatL8h9s"
      },
      "source": [
        "##Gitへの登録"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JIY5cl_4DCQS"
      },
      "source": [
        "!git config --global user.email \"92.sky.428@gmail.com\"\n",
        "!git config --global user.name \"ShuheiKuraoka\""
      ],
      "execution_count": 12,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mPxojV2_0NjJ",
        "outputId": "f4b915ad-d8d0-4e07-cc0f-485f26cbe7c9"
      },
      "source": [
        "!git init"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Reinitialized existing Git repository in /content/.git/\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pDxCSaen0i5f",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "afe06dd6-f9bb-4b80-fbf4-dfce267f520c"
      },
      "source": [
        "!git remote add origin https://github.com/ShuheiKuraoka/Streamlit.git"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "fatal: remote origin already exists.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 224
        },
        "id": "2cN4KALV1V4k",
        "outputId": "41e387c5-6915-4192-980d-0435e32c6b41"
      },
      "source": [
        "!git clone  https://github.com/ShuheiKuraoka/Speesh-to-Text_streamlit_app.git\n",
        "Username: ShuheiKuraoka\n",
        "Password: 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"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "fatal: destination path 'Speesh-to-Text_streamlit_app' already exists and is not an empty directory.\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-2-12538e59a315>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0mget_ipython\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msystem\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'git clone  https://github.com/ShuheiKuraoka/Speesh-to-Text_streamlit_app.git'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 2\u001b[0;31m \u001b[0mUsername\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mShuheiKuraoka\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      3\u001b[0m \u001b[0mPassword\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0m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\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'ShuheiKuraoka' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Itif4QdT6SGU"
      },
      "source": [
        "!git add /content/drive/MyDrive/Streamlit_App_Github/Speesh-to-Text_streamlit_app.py\n",
        "#\n",
        "#!git add ."
      ],
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tJPJVyBkN-_s",
        "outputId": "2674491f-23b6-4f98-e451-7fc8e1ce700f"
      },
      "source": [
        "#git addの取り消し\n",
        "#全てのファイル1回目\n",
        "!git rm --cached -r .\n",
        "#特定のファイルのみ1回目\n",
        "#git rm –cached -r　ファイル名\n",
        "#全てのファイル2回目以降\n",
        "#git reset HEAD\n",
        "#特定のファイル2回目以降\n",
        "#git reset HEAD ファイル名"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "fatal: pathspec '.' did not match any files\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rajP_eQ2AJC0",
        "outputId": "e51c8174-c71d-44d9-bedd-810e0428585f"
      },
      "source": [
        "!git commit -m \"1st commit \""
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[master (root-commit) 91a4b6a] 1st commit\n",
            " 1 file changed, 58 insertions(+)\n",
            " create mode 100644 drive/MyDrive/Streamlit_App_Github/Speesh-to-Text_streamlit_app.py\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mc8jzAL8UDUq",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5f52a0e0-3b4d-492a-e2cc-bc3a23e241f2"
      },
      "source": [
        "#コミット履歴の閲覧\n",
        "!git log"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "fatal: your current branch 'master' does not have any commits yet\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sMWrIlX5UyTr",
        "outputId": "2de77f46-43c4-41d1-f736-1e02369fcc3a"
      },
      "source": [
        "#コミットの取り消し\n",
        "!git reset --hard HEAD^"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "fatal: ambiguous argument 'HEAD^': unknown revision or path not in the working tree.\n",
            "Use '--' to separate paths from revisions, like this:\n",
            "'git <command> [<revision>...] -- [<file>...]'\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "0Ypz2uvvVlwy",
        "outputId": "9d0070ac-64e4-4679-ec2c-b1ea14f3e0fd"
      },
      "source": [
        "#失敗したコミットを修正したい時\n",
        "!git commit --amend -m \"1st commit\""
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "fatal: You have nothing to amend.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m6qw_VLGIE6O",
        "outputId": "d4994e46-10ac-487d-c5b5-b387c8e0ee1f"
      },
      "source": [
        "#!git status"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "On branch main\n",
            "nothing to commit, working tree clean\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lBzZ0b7JXgCD"
      },
      "source": [
        "#untracked fileを削除(事前準備)\n",
        "#削除対象ファイルの確認\n",
        "!git clean -m\n",
        "#ディレクトリの確認\n",
        "#!git clean -dn"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Phub8zvAZlr4",
        "outputId": "1d8db0a6-ec33-4cbb-b2ba-5f82c50e023b"
      },
      "source": [
        "#untracked fileを削除\n",
        "#!git clean -f\n",
        "#ディレクトリの削除\n",
        "#!git clean -df"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Removing .config/\n",
            "Removing .ipynb_checkpoints/\n",
            "warning: failed to remove drive/.Trash-0/files: No such file or directory\n",
            "warning: failed to remove drive/.Trash-0/info: No such file or directory\n",
            "warning: failed to remove drive/.file-revisions-by-id/: Operation canceled\n",
            "warning: failed to remove drive/.shortcut-targets-by-id/: Operation canceled\n",
            "Removing drive/MyDrive/.ipynb_checkpoints/\n",
            "Removing \"drive/MyDrive/AI\\346\\225\\231\\350\\202\\262\\351\\226\\213\\347\\231\\272\\351\\203\\250\\351\\226\\242\\351\\200\\243 (1)/\"\n",
            "Removing drive/MyDrive/Colab Notebooks/\n",
            "Removing drive/MyDrive/ML0001/\n",
            "Removing drive/MyDrive/PY0001/\n",
            "Removing sample_data/\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qu4uqhQEQl81",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "528a2e37-3999-4a4d-acb9-ae459d432123"
      },
      "source": [
        "#現在登録されているリモートリポジトリの確認\n",
        "!git remote -v "
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "fatal: not a git repository (or any of the parent directories): .git\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qXhI9VUFQ5vq",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8ff8071d-c7bd-46a6-abad-b3385df748ee"
      },
      "source": [
        "#git remote add の取り消し\n",
        "!git remote rm origin"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "fatal: not a git repository (or any of the parent directories): .git\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uYfd_UURGMF3"
      },
      "source": [
        "!git branch -M main"
      ],
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EsSqinCt8wNs",
        "outputId": "755c064c-708b-49e3-a525-0ed97eba8d36"
      },
      "source": [
        "!git push origin main\n",
        "#!git push origin :main\n",
        "#!git push -u origin main\n",
        "#!git push origin master\n",
        "#→エラーが出てしまうのは、レポジトリ名が原因です。\n",
        "#以前は「master」ブランチが自動で作成されていたのですが、2020/10以降、新規にレポジトリを作成すると、「main」ブランチが作成されます。\n",
        "#git push origin masterでpushしようとすると、レポジトリ名が異なるため、エラーになってしまうということです。\n",
        "#これまでに作成したレポジトリは、変更していないと、「master」ブランチであるということにも注意です。"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "fatal: could not read Username for 'https://github.com': No such device or address\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "me00eSijvBQg",
        "outputId": "fa875672-956b-40bd-9cb8-9fd63634fff0"
      },
      "source": [
        "!git pull origin main"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "fatal: Couldn't find remote ref main\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vD7aex7gdc3P"
      },
      "source": [
        "#GitHubにpush出来なかったら\n",
        "#!git remote set-url origin https://ShuheiKuraoka:s040428k@github.com/ShuheiKuraok/Speesh-to-Text_streamlit_app.git\n",
        "#8月13日以降パスワード認証が出来なくなりました。"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qyGIp_T2wb7_",
        "outputId": "f7cffcca-8b9f-48d7-f2c2-65cd83d5a33f"
      },
      "source": [
        "!git fetch origin\n",
        "!git merge --allow-unrelated-histories origin/main"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "merge: origin/main - not something we can merge\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "B0QKTu4WBFqI",
        "outputId": "8dbcdf04-2e9f-4eed-9c69-9fdd8cb73469"
      },
      "source": [
        "!ls -al /content/Agent"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "-rw-r--r-- 1 root root 15 Aug 16 06:40 /content/Agent\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w39eUew3qLDx",
        "outputId": "e3ac3533-bedc-4d4c-d913-94513be12303"
      },
      "source": [
        "!ssh-keygen -t ed25519 -C \"92.sky.428@gmail.com\""
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Generating public/private ed25519 key pair.\n",
            "Enter file in which to save the key (/root/.ssh/id_ed25519): \n",
            "/root/.ssh/id_ed25519 already exists.\n",
            "Overwrite (y/n)? y\n",
            "Enter passphrase (empty for no passphrase): sky040428\n",
            "Enter same passphrase again: sky040428\n",
            "Your identification has been saved in /root/.ssh/id_ed25519.\n",
            "Your public key has been saved in /root/.ssh/id_ed25519.pub.\n",
            "The key fingerprint is:\n",
            "SHA256:k2xjxbtjPdSwqT13qHNXk9zw9jAyJ6gKekH31MgzblQ 92.sky.428@gmail.com\n",
            "The key's randomart image is:\n",
            "+--[ED25519 256]--+\n",
            "|                 |\n",
            "|         .E      |\n",
            "|       . +o .    |\n",
            "|    . ..Bo.. =.  |\n",
            "|   . . =So..+ ooo|\n",
            "|    .  o+o.*+ +==|\n",
            "|    .. . .= ==o+=|\n",
            "|   ...  .. ..=..o|\n",
            "|  ..  ..    .o . |\n",
            "+----[SHA256]-----+\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "GsuA3sh7s4ii",
        "outputId": "7a2d05b9-d3aa-4cbc-bd21-9f9fefac4b6c"
      },
      "source": [
        "!eval \"$(ssh-agent -s)\""
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Agent pid 5422\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Uz-2Cvd3tr-_",
        "outputId": "61cea9c4-3dd6-4d93-c93d-e7b4b6b360f1"
      },
      "source": [
        "!ssh-add   /root/.ssh/id_ed25519.pub"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Could not open a connection to your authentication agent.\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PlWlGXunAICh",
        "outputId": "5aa8f9c4-0331-4620-9bf1-03cb3258fbba"
      },
      "source": [
        "!clip < /root/.ssh/id_ed25519.pub"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "/bin/bash: clip: command not found\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IQvsMk31SJob"
      },
      "source": [
        ""
      ]
    }
  ]
}