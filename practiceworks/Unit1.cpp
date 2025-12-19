//---------------------------------------------------------------------------
// Практична робота №10 Рукасов Владислав 
#include <vcl.h>
#pragma hdrstop

#include "Unit1.h"
#include <math.h>

#pragma package(smart_init)
#pragma resource "*.dfm"

TForm1 *Form1;

// -------------------------------------------------------------
//             Базовий клас вузла дерева
// -------------------------------------------------------------
class Telement
{
public:
    virtual double rezult() = 0;
    virtual ~Telement() {}
};

// -------------------------------------------------------------
//             Клас числа
// -------------------------------------------------------------
class Number : public Telement
{
public:
    double value;

    Number(double v)
    {
        value = v;
    }

    double rezult()
    {
        return value;
    }
};

// -------------------------------------------------------------
//             Клас змінної x
// -------------------------------------------------------------
double value_x; // глобальне значення x

class X : public Telement
{
public:
    X() {}

    double rezult()
    {
        return value_x;
    }
};

// -------------------------------------------------------------
//             Клас змінної y   (новий — для f(x, y))
// -------------------------------------------------------------
double value_y; // глобальне значення y

class Y : public Telement
{
public:
    Y() {}

    double rezult()
    {
        return value_y;
    }
};

// -------------------------------------------------------------
//             Операція додавання
// -------------------------------------------------------------
class Plus : public Telement
{
public:
    Telement *left, *right;

    Plus(Telement *l, Telement *r)
    {
        left = l;
        right = r;
    }

    double rezult()
    {
        return left->rezult() + right->rezult();
    }
};

// -------------------------------------------------------------
//             Операція множення
// -------------------------------------------------------------
class Mult : public Telement
{
public:
    Telement *left, *right;

    Mult(Telement *l, Telement *r)
    {
        left = l;
        right = r;
    }

    double rezult()
    {
        return left->rezult() * right->rezult();
    }
};

// -------------------------------------------------------------
//             Функція побудови дерева (розбір виразу)
// -------------------------------------------------------------
AnsiString s; // вираз
int i;        // позиція в рядку

Telement* form(); // прототип

Telement* term(); // множення
Telement* factor(); // число / змінна

// ----------------------
// Функція form()
// ----------------------
Telement* form()
{
    return term();
}

// ----------------------
// Розбір множення та додавання
// ----------------------
Telement* term()
{
    Telement *p = factor();

    while (i <= s.Length())
    {
        if (s[i] == '+')
        {
            i++;
            p = new Plus(p, factor());
        }
        else if (s[i] == '*')
        {
            i++;
            p = new Mult(p, factor());
        }
        else
            break;
    }
    return p;
}

// ----------------------
// Розбір чисел і змінних
// ----------------------
Telement* factor()
{
    // Число
    if (s[i] >= '0' && s[i] <= '9')
    {
        double val = 0;
        while (i <= s.Length() && (s[i] >= '0' && s[i] <= '9'))
        {
            val = val * 10 + (s[i] - '0');
            i++;
        }

        // дробова частина
        if (i <= s.Length() && s[i] == DecimalSeparator)
        {
            i++;
            double k = 0.1;
            while (i <= s.Length() && (s[i] >= '0' && s[i] <= '9'))
            {
                val += k * (s[i] - '0');
                k *= 0.1;
                i++;
            }
        }

        return new Number(val);
    }

    // змінна x
    if (s[i] == 'x')
    {
        i++;
        return new X();
    }

    // змінна y  (нова)
    if (s[i] == 'y')
    {
        i++;
        return new Y();
    }

    return new Number(0); // fallback
}

//---------------------------------------------------------------------------
//                  Кнопка "Обчислити"
//---------------------------------------------------------------------------
void __fastcall TForm1::Button1Click(TObject *Sender)
{
    int dec = StrToInt(ComboBox1->Text);

    value_x = StrToFloat(Edit1->Text);  // x
    value_y = StrToFloat(Edit8->Text);  // y (нова змінна)

    s = Edit2->Text;  // вираз f(x, y)
    i = 1;

    Telement *fx = form();
    Edit4->Text = FloatToStrF(fx->rezult(), ffFixed, 25, dec);

    delete fx;
}

//---------------------------------------------------------------------------
//           Кнопка "Побудувати дерево" для 3*4+2
//---------------------------------------------------------------------------
void __fastcall TForm1::Button3Click(TObject *Sender)
{
    Number n3(3);
    Number n4(4);
    Number a(2);

    Mult m(&n3, &n4); // 3*4
    Plus p(&m, &a);   // (3*4)+2

    Edit5->Text = FloatToStrF(p.rezult(), ffFixed, 25, 8);
    Edit6->Text = FloatToStrF(m.rezult(), ffFixed, 25, 8);
    Edit7->Text = FloatToStrF(a.rezult(), ffFixed, 25, 8);
}

//---------------------------------------------------------------------------
//     Комбо-бокс зміни точності — повторно обчислює результат
//---------------------------------------------------------------------------
void __fastcall TForm1::ComboBox1Change(TObject *Sender)
{
    Button1Click(Button1);
}
//---------------------------------------------------------------------------